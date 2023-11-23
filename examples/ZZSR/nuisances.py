mcProduction = 'Summer20UL18_106x_nAODv9_Full2018v9'
dataReco = 'Run2018_UL2018_nAODv9_Full2018v9'
mcSteps = 'MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9'
fakeSteps = 'DATAl1loose2018v9__l2loose__fakeW'
dataSteps = 'DATAl1loose2018v9__l2loose__l2tightOR2018v9'

#limitFiles = -1

print(treeBaseDir)
def makeMCDirectory(var=''):
    _treeBaseDir = treeBaseDir + ''
    if useXROOTD:
        _treeBaseDir = redirector + treeBaseDir
    if var== '':
        return '/'.join([_treeBaseDir, mcProduction, mcSteps])
    else:
        return '/'.join([_treeBaseDir, mcProduction, mcSteps + '__' + var])


# merge cuts
_mergedCuts = []
for cut in list(cuts.keys()):
    __cutExpr = ''
    if type(cuts[cut]) == dict:
        __cutExpr = cuts[cut]['expr']
        for cat in list(cuts[cut]['categories'].keys()):
            _mergedCuts.append(cut + '_' + cat)
    elif type(cuts[cut]) == str:
        _mergedCuts.append(cut)

cuts2j = _mergedCuts

nuisances = {}

nuisances['lumi']  = {
    'name'  : 'lumi_13TeV_2017',
    'type'  : 'lnN',
    'samples'  : {
        #'DY'       : '1.023',    |
        #'top'      : '1.023',    | These 3 backgrounds are data driven, no need to include the luminosity uncertainty
        #'WW'       : '1.023',    |
        'Vg'       : '1.023',
        #'VgS'      : '1.023',
        #'WZgS'     : '1.023',
        #'WZgS_L'   : '1.023',
        #'WZgS_H'   : '1.023',
        'ZZ'   : '1.023',
        #'WZ'       : '1.023',
        'VVV'      : '1.023',
        #'DPS'  : '1.023',
        #'WW_strong'  : '1.023',
        #'WpWp_EWK'   : '1.023',
    }
}

autoStats = False
if autoStats:
    ## Use the following if you want to apply the automatic combine MC stat nuisances.
    nuisances['stat'] = {
        'type': 'auto',
        'maxPoiss': '10',
        'includeSignal': '0',
        #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
        #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
        'samples': {}
    }
