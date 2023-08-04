import ROOT
import uproot
from fnmatch import fnmatch
from mkShapesRDF.processor.framework.module import Module
import sys
import subprocess


class Snapshot(Module):
    """
    The Snapshot module handles the creation of the final output files.
    There are 4 possible scenarios:

    - snapshot nominals only
    - snapshot variations only in separate files (one file per variation)
    - snapshot nominals and variation in separate files (one file per variation and one file for nominal)
    - snapshot both nominals and variations in the same file

    The module does not run the snapshotting itself, but it creates the Snapshot objects with lazy evaluation.
    The snapshots to be run are added to the ``values`` variable:

    .. code-block:: python

        values.append(
            [
                "snapshot",
                SnapshotObject,
                [tmpOutputFilename, copyFromInputFiles , outputFolderPath, outputFilenameEOS]
            ])

    Where

    - ``tmpOutputFilename`` is the name of the temporary output file,
    - ``copyFromInputFiles`` is a boolean that indicates if the  auxiliary keys of the input files should be copied in the output (only done for nominals),
    - ``outputFolderPath`` is the path of the output folder
    - ``outputFilenameEOS`` is the name of the output file in the EOS folder (final output file name)

    """

    def __init__(
        self,
        tmpOutputFilename,
        columns,
        eosPath,
        outputFilename,
        includeVariations=True,
        splitVariations=True,
        storeNominals=True,
    ):
        super().__init__("Snapshot")
        self.tmpOutputFilename = tmpOutputFilename
        self.columns = columns

        self.eosPath = eosPath
        self.outputFilename = outputFilename

        self.includeVariations = includeVariations
        self.splitVariations = splitVariations
        self.storeNominals = storeNominals

    @staticmethod
    def CopyFromInputFiles(outputFilename, inputFiles):
        """
        Copy the auxiliary keys from the input files into the output file.

        It ``hadd``s the input files into a temporary file, then it copies the keys from the temporary file into the output file.

        Parameters
        ----------
        outputFilename : str
            The name of the output file where to copy the keys (should be equal to ``tmpOutputFilename``)
        inputFiles : `list of str`
            The list of input files from which to copy the keys

        """
        # copy other information from inputFiles into the outputfile

        
        if len(inputFiles)>1:
            mergedOutput = f"merged_{outputFilename}"
            
            proc = subprocess.Popen(
                f'hadd -fk {mergedOutput} {" ".join(inputFiles)}',
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            out, err = proc.communicate()
            print(out.decode("utf-8"))
            print(err.decode("utf-8"), file=sys.stderr)
        else:
            mergedOutput = inputFiles[0]


        print("DOING SOMETHING")

        f = uproot.open(mergedOutput)
        f2 = uproot.update(outputFilename)

        Element_branches = []

        trees = [k for k in f.keys() if "Events" not in k]

        for tree in trees:

            if "TTree" not in str(type(f[tree])):
                if "String" in str(type(f[tree])):
                    f2[tree] = str(f[tree])
                else:
                    f2[tree] = f[tree].array()
            else:

                TBElementInTTree = False

                for col in f[tree].keys():
                    
                    ### Trick for ParameterSet and Metadata   /  Cannot be added with uproot
                    if "TBranchElement" in str(type(f[tree][col])):
                        Element_branches.append(tree)
                        TBElementInTTree = True
                        break

                if TBElementInTTree: continue

                input_tree = f[tree]
                first = True
                for arrays_chunk in input_tree.iterate(step_size="100 MB", how=dict):
                    if first:
                        f2[tree] = arrays_chunk
                        first = False
                    else:
                        f2[tree].extend(arrays_chunk)

        f.close()
        f2.close()

        ### Try in the traditional way
        if len(Element_branches)!=0:
            f = ROOT.TFile.Open(mergedOutput)
            f2 = ROOT.TFile.Open(outputFilename, "UPDATE")

            for tree in Element_branches:
                f2.cd()
                f.Get(tree).Write()

            f2.Close()
            f.Close()


        '''
        f = ROOT.TFile.Open(mergedOutput)
        f2 = ROOT.TFile(outputFilename, "UPDATE")

        trees = [k.GetName() for k in f.GetListOfKeys()]
        trees = list(set(trees).difference(set(["Events"])))

        f2.cd()
        for key in trees:
            f.Get(key).Write()
        f2.Close()
        f.Close()
        '''
        proc = subprocess.Popen(
            f"rm {mergedOutput}",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = proc.communicate()
        print(out.decode("utf-8"))
        print(err.decode("utf-8"), file=sys.stderr)
        


    def SplitVariations(self, df):
        """
        Create a Snapshot object for each variation and tag.

        Parameters
        ----------
        df : mRDF
            The ``mRDF`` object to use for snapshot

        """
        # create separate files for each variation and tag
        for variationName in df.variations:
            for tag in df.variations[variationName]["tags"]:
                tmp_varied_cols = df.GetVariedColumns_oneVariation(
                    self.saveColumns, variationName, tag
                )
                outputFilename = self.tmpOutputFilename.split(".")
                outputFilename[-2] += "__" + variationName + "_" + tag
                outputFilename = ".".join(outputFilename)
                self.snapshots.append(
                    [
                        variationName + "_" + tag,
                        tmp_varied_cols,
                        outputFilename,
                        False,
                        self.eosPath + "__" + variationName + "_" + tag,
                        self.outputFilename,
                    ]
                )

    def StoreNominals(self, df):
        """
        Create a Snapshot object for the nominal columns.

        Parameters
        ----------
        df : mRDF
            The ``mRDF`` object to use for snapshot
        """
        # store only nominals and remove variations from the list
        tmp_varied_cols = df.GetVariedColumns(self.saveColumns)
        saveColumns = list(set(self.saveColumns).difference(set(tmp_varied_cols)))
        self.snapshots.append(
            [
                "nominal",
                saveColumns,
                self.tmpOutputFilename,
                True,
                self.eosPath,
                self.outputFilename,
            ]
        )

    def StoreNominalsAndVariations(self, df):
        """
        Create a Snapshot object containing both nominals and variations.

        Parameters
        ----------
        df : mRDF
            The ``mRDF`` object to use for snapshot

        """
        # store variation in the same file as nominal
        tmp_varied_cols = df.GetVariedColumns(self.saveColumns)
        self.snapshots.append(
            [
                "nominal and varied",
                self.saveColumns + tmp_varied_cols,
                self.tmpOutputFilename,
                True,
                self.eosPath,
                self.outputFilename,
            ]
        )

    def runModule(self, df, values):
        print("Snapshotting to", self.outputFilename, "columns:\n", self.columns)

        cols = df.GetColumnNames()
        saveColumns = []
        for pattern in self.columns:
            tmp_cols = list(set(filter(lambda k: fnmatch(k, pattern), cols)))
            if len(tmp_cols) == 0:
                print("Warning: no columns found to snapshot with pattern", pattern)
            saveColumns = list(set(saveColumns).union(set(tmp_cols)))

        self.saveColumns = list(set(saveColumns))

        self.snapshots = []

        if self.includeVariations and self.splitVariations and self.storeNominals:
            self.SplitVariations(df)
            self.StoreNominals(df)

        if self.includeVariations and self.splitVariations and not self.storeNominals:
            self.SplitVariations(df)

        if (
            self.includeVariations
            and not self.splitVariations
            and not self.storeNominals
        ):
            print(
                "Cannot snapshot variations all together without storing nominal\nEither set storeNominals=True or splitVariations=True",
                file=sys.stderr,
            )
            sys.exit(1)

        if (
            not self.includeVariations
            and not self.splitVariations
            and not self.storeNominals
        ):
            print(
                "Snapshot without variations and without storing nominal is not supported",
                file=sys.stderr,
            )
            sys.exit(1)

        if (
            not self.includeVariations
            and self.splitVariations
            and not self.storeNominals
        ):
            print(
                "Snapshot without variations and with split variations is not supported\nTurn on includeVariations",
                file=sys.stderr,
            )
            sys.exit(1)

        if not self.includeVariations and self.splitVariations and self.storeNominals:
            print(
                "Snapshot without variations and with split variations is not supported\nTurn on includeVariations",
                file=sys.stderr,
            )
            sys.exit(1)

        if (
            not self.includeVariations
            and not self.splitVariations
            and self.storeNominals
        ):
            self.StoreNominals(df)

        if self.includeVariations and not self.splitVariations and self.storeNominals:
            self.StoreNominalsAndVariations(df)

        for snapshot in self.snapshots:
            _cols = sorted(list(set(snapshot[1])))
            print("Final list of variables for snapshot", snapshot[0], _cols)
            opts = ROOT.RDF.RSnapshotOptions()
            opts.fLazy = True
            opts.fMode = "UPDATE"
            opts.fOverwriteIfExists = True
            opts.fCompressionAlgorithm = ROOT.ROOT.kLZMA
            opts.fCompressionLevel = 9
            values.append(
                [
                    "snapshot",
                    df.Snapshot("Events", snapshot[2], _cols, opts),
                    snapshot[2:],
                ]
            )

        return df
