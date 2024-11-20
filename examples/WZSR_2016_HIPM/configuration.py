# example of configuration file
treeName= 'Events'
date='_2016_HIPM'
tag = 'VBS_WZ'+date
runnerFile = 'default'

# used by mkShape to define output directory for root files
#outputDir = 'rootFile'+date

outputFile    = "mkShapes__{}.root".format(tag)
outputFolder  = "rootFiles__{}".format(tag)
batchFolder   = 'condor'
configsFolder = 'configs'

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py'

# file with list of samples
samplesFile = 'samples.py'

# file with list of samples
plotFile = 'plot.py'

# structure file for datacard
structureFile = 'structure.py'


# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'

# luminosity to normalize to (in 1/fb)
lumi = 19.5

plotPath = 'plots_' + tag
outputDirDatacard = 'datacards'


minRatio = 0.5
maxRatio = 1.5
plotPath      = "plots__{}".format(tag)


mountEOS=[]
imports = ["os", "glob", ("collections", "OrderedDict"), "ROOT"]
filesToExec = [
    samplesFile,
    cutsFile,
    aliasesFile,
    variablesFile,
    plotFile,
    nuisancesFile,
    structureFile,
]

varsToKeep = [
    "batchVars",
    "outputFolder",
    "batchFolder",
    "configsFolder",
    "outputFile",
    "runnerFile",
    "tag",
    "samples",
    "aliases",
    "variables",
    ("cuts", {"cuts": "cuts", "preselections": "preselections"}),
    ("plot", {"plot": "plot", "groupPlot": "groupPlot", "legend": "legend"}),
    "nuisances",
    "structure",
    "lumi",
    "mountEOS",
]

batchVars = varsToKeep[varsToKeep.index("samples") :]

varsToKeep += ['minRatio', 'maxRatio', 'plotPath']



