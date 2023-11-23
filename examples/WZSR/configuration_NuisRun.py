# example of configuration file
treeName= 'Events'

#date='_Nov252018_ptll'
date='_2018_31082022_NuisRun'

tag = 'VBS_WZ'+date


# used by mkShape to define output directory for root files
outputDir = 'rootFile'+date

# file with TTree aliases
aliasesFile = 'aliases_310822.py'

# file with list of variables
variablesFile = 'variables_NuisRun.py'

# file with list of cuts
cutsFile = 'cuts_NuisRun.py'
#cutsFile = 'cuts_forPlots.py'

# file with list of samples
samplesFile = 'samples_310822.py'

# file with list of samples
plotFile = 'plot_310822.py'

# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plotVBS'+date


# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards'+date


# structure file for datacard
structureFile = 'structure.py'


# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances_NuisRun.py'
