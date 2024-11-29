import os, glob
mcProduction = 'Summer20UL16_106x_nAODv9_noHIPM_Full2016v9'
dataReco = 'Run2016_UL2016_nAODv9_noHIPM_Full2016v9'
mcSteps = 'MCl1loose2016v9__MCCorr2016v9NoJERInHorn__l2tightOR2016v9'
fakeSteps = 'DATAl1loose2016v9__l2loose__fakeW'
dataSteps = 'DATAl1loose2016v9__l2loose__l2tightOR2016v9'

##############################################
###### Tree base directory for the site ######
##############################################
treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
limitFiles = -1


def makeMCDirectory(var=""):
    _treeBaseDir = treeBaseDir + ""
    if var == "":
        return "/".join([_treeBaseDir, mcProduction, mcSteps])
    else:
        return "/".join([_treeBaseDir, mcProduction, mcSteps + "__" + var])

mcDirectory = makeMCDirectory()
fakeDirectory = os.path.join(treeBaseDir, dataReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)

samples = {}

from mkShapesRDF.lib.search_files import SearchFiles
searchFiles = SearchFiles()

useXROOTD = False
redirector = 'root://eoscms.cern.ch/'
redirector2 = 'root://eoshome-c.cern.ch/'

## For SM ##

def nanoGetSampleFiles(path, name):
    _files = searchFiles.searchFiles(path, name, redirector=redirector)
    if limitFiles != -1 and len(_files) > limitFiles:
        return [(name, _files[:limitFiles])]
    else:
        return  [(name, _files)]
    
## For EFT ##

def nanoGetSampleFiles2(path, name):
    _files = searchFiles.searchFiles(path, name, redirector=redirector2)
    if limitFiles != -1 and len(_files) > limitFiles:
        return [(name, _files[:limitFiles])]
    else:
        return  [(name, _files)]
        
def CombineBaseW(samples, proc, samplelist):
    _filtFiles = list(filter(lambda k: k[0] in samplelist, samples[proc]['name']))
    _files = list(map(lambda k: k[1], _filtFiles))
    _l = list(map(lambda k: len(k), _files))
    leastFiles = _files[_l.index(min(_l))]
    dfSmall = ROOT.RDataFrame("Runs", leastFiles)
    s = dfSmall.Sum('genEventSumw').GetValue()
    f = ROOT.TFile(leastFiles[0])
    t = f.Get("Events")
    t.GetEntry(1)
    xs = t.baseW * s

    __files = []
    for f in _files:
        __files += f
    df = ROOT.RDataFrame("Runs", __files)
    s = df.Sum('genEventSumw').GetValue()
    newbaseW = str(xs / s)
    weight = newbaseW + '/baseW'

    for iSample in samplelist:
        addSampleWeight(samples, proc, iSample, weight) 

def addSampleWeight(samples, sampleName, sampleNameType, weight):
    obj = list(filter(lambda k: k[0] == sampleNameType, samples[sampleName]['name']))[0]
    samples[sampleName]['name'] = list(filter(lambda k: k[0] != sampleNameType, samples[sampleName]['name']))
    if len(obj) > 2:
        samples[sampleName]['name'].append((obj[0], obj[1], obj[2] + '*(' + weight + ')'))
    else:
        samples[sampleName]['name'].append((obj[0], obj[1], '(' + weight + ')' ))

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
    ['F','Run2016F-UL2016-v1'],
    ['G','Run2016G_UL2016-v1'],
    ['H','Run2016H_UL2016-v1'],
]

DataSets = ['MuonEG','SingleMuon','SingleElectron','DoubleMuon', 'DoubleEG']

DataTrig = {
    'MuonEG'         : ' Trigger_ElMu' ,
    'SingleMuon'     : '!Trigger_ElMu && Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_ElMu && !Trigger_sngMu && Trigger_sngEl',
    'DoubleMuon'     : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && Trigger_dblMu',
    'DoubleEG'       : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && !Trigger_dblMu && Trigger_dblEl'
}

################################################
############ BASIC MC WEIGHTS ##################
################################################

Nlep='3'

eleWP = 'mvaFall17V2Iso_WP90_tthmva_70'
#muWP  = 'cut_Tight_HWWW_tthmva_80'
muWP = 'cut_Tight80x_tthmva_80'

LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

XSWeight      = 'XSWeight'
SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut
PromptGenLepMatch   = 'PromptGenLepMatch'+Nlep+'l'

mcCommonWeight = 'SFweight_mod*btagSF*'+PromptGenLepMatch
mcCommonWeightNoMatch = 'SFweight_mod*btagSF'
mcCommonWeightOS =  'SFweight_mod*btagSF*'+PromptGenLepMatch+'*oppositesign_requirement'
# btag SF here bc maybe its different from the one of the central samples

###########################################
#############  EFT WEIGHTS  ###############
#############   No mixed!   ###############
###########################################

rwgt_sm = '(LHEReweightingWeight[0])'
rwgt_sm_lin_quad_cW = '(LHEReweightingWeight[1])'
rwgt_quad_cW = '(0.5*(1/1)*(1/1)*(LHEReweightingWeight[1] + LHEReweightingWeight[2] - 2*LHEReweightingWeight[0]))'
rwgt_sm_lin_quad_cHbox = '(LHEReweightingWeight[3])'
rwgt_quad_cHbox = '(0.5*(1/1)*(1/1)*(LHEReweightingWeight[3] + LHEReweightingWeight[4] - 2*LHEReweightingWeight[0]))'
rwgt_sm_lin_quad_cHDD = '(LHEReweightingWeight[5])'
rwgt_quad_cHDD = '(0.5*(1/1)*(1/1)*(LHEReweightingWeight[5] + LHEReweightingWeight[6] - 2*LHEReweightingWeight[0]))'
rwgt_sm_lin_quad_cHW = '(LHEReweightingWeight[7])'
rwgt_quad_cHW = '(0.5*(1/1)*(1/1)*(LHEReweightingWeight[7] + LHEReweightingWeight[8] - 2*LHEReweightingWeight[0]))'
rwgt_sm_lin_quad_cHWB = '(LHEReweightingWeight[9])'
rwgt_quad_cHWB = '(0.5*(1/1)*(1/1)*(LHEReweightingWeight[9] + LHEReweightingWeight[10] - 2*LHEReweightingWeight[0]))'

rwgt_sm_lin_quad_mixed_cW_cHbox = '(LHEReweightingWeight[11])'
rwgt_sm_lin_quad_mixed_cW_cHDD = '(LHEReweightingWeight[12])'
rwgt_sm_lin_quad_mixed_cW_cHW = '(LHEReweightingWeight[13])'
rwgt_sm_lin_quad_mixed_cW_cHWB = '(LHEReweightingWeight[14])'
rwgt_sm_lin_quad_mixed_cHbox_cHDD = '(LHEReweightingWeight[15])'
rwgt_sm_lin_quad_mixed_cHbox_cHW = '(LHEReweightingWeight[16])'
rwgt_sm_lin_quad_mixed_cHbox_cHWB = '(LHEReweightingWeight[17])'
rwgt_sm_lin_quad_mixed_cHDD_cHW = '(LHEReweightingWeight[18])'
rwgt_sm_lin_quad_mixed_cHDD_cHWB = '(LHEReweightingWeight[19])'
rwgt_sm_lin_quad_mixed_cHW_cHWB = '(LHEReweightingWeight[20])'

###########################################
#############  BACKGROUNDS  ###############
###########################################

## WZ SM ##

files = nanoGetSampleFiles(mcDirectory, 'WLLJJ_WToLNu_EWK_UL')
samples['sm'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu')
samples['WZ_QCD'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

## ZZ To 4L && ZZ To 2Q2L ##

samples['ZZ'] = {  'name'  : nanoGetSampleFiles(mcDirectory,'ZZTo2Q2L_mllmin4p0') + \
                             nanoGetSampleFiles(mcDirectory,'ZZTo2L2Nu') + \
                             nanoGetSampleFiles(mcDirectory,'ZZTo4L'),
                    'weight' :  XSWeight+'*'+SFweight+'*((nLepton==3)*PromptGenLepMatch3l + (nLepton>3)*PromptGenLepMatch4l)*'+METFilter_MC,
                    'FilesPerJob' : 3,
                 }

## tVx ##

files = nanoGetSampleFiles(mcDirectory, 'TTZToLLNuNu_M-10') + \
        nanoGetSampleFiles(mcDirectory, 'TTWJetsToLNu') + \
        nanoGetSampleFiles(mcDirectory, 'tZq_ll_4f')
samples['tVx'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

## VgS1 ##

#files = nanoGetSampleFiles(mcDirectory, 'ZGToLLG') + \
#        nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin0p1')
#samples['VgS1'] = {
#    'name': files,
#    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
#    'FilesPerJob': 4,
#    'subsamples': {
#        'L': 'gstarLow',
#        'H': 'gstarHigh'
#    }
#}
#addSampleWeight(samples, 'VgS1', 'ZGToLLG', '(Gen_ZGstar_mass > 0)')
#addSampleWeight(samples, 'VgS1', 'WZTo3LNu_mllmin0p1', '(Gen_ZGstar_mass > 0.1 && Gen_ZGstar_mass<4)')


## VgS ##

files = nanoGetSampleFiles(mcDirectory, 'WGToLNuG') + \
        nanoGetSampleFiles(mcDirectory, 'ZGToLLG')
samples['VgS'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'FilesPerJob': 4,
    'subsamples': {
      'L': 'gstarLow',
      'H': 'gstarHigh'
    }
}
addSampleWeight(samples, 'VgS', 'WGToLNuG', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass <= 4.0)')
addSampleWeight(samples, 'VgS', 'ZGToLLG', '(Gen_ZGstar_mass > 0)')

## VVV ##

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWW')
samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

## Top ##
#
#files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
#        nanoGetSampleFiles(mcDirectory, 'TTToSemiLeptonic') + \
#        nanoGetSampleFiles(mcDirectory, 'ST_tW_top') + \
#        nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop')
#samples['Top'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 4
#}

## Top ##

files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
         nanoGetSampleFiles(mcDirectory, 'ST_s-channel') + \
         nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
         nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
         nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop') + \
         nanoGetSampleFiles(mcDirectory, 'ST_tW_top')

samples['Top'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5,
}

###########################################
################## FAKE ###################
###########################################

samples['Fake_lep'] = {
  'name': [],
  'weight': 'METFilter_DATA*fakeW',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 20
}

for _, sd in DataRun:
  for pd in DataSets:
    tag = pd + '_' + sd
    if 'DoubleMuon' in pd and 'Run2016G' in sd:
        print("sd      = {}".format(sd))
        print("pd      = {}".format(pd))
        print("Old tag = {}".format(tag))
        tag = tag.replace('v1','v2')
        print("New tag = {}".format(tag))

    files = nanoGetSampleFiles(fakeDirectory,tag)

    samples['Fake_lep']['name'].extend(files)
    samples['Fake_lep']['weights'].extend([DataTrig[pd]] * len(files))
    addSampleWeight(samples, 'Fake_lep', tag, DataTrig[pd])

samples['Fake_lep']['subsamples'] = {
  'em': 'abs(Lepton_pdgId[0]) == 11',
  'me': 'abs(Lepton_pdgId[0]) == 13'
}

###########################################
################## DATA ###################
###########################################

samples['DATA'] = {
  'name': [],
  'weight': 'LepWPCut*METFilter_DATA',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 50
}

for _, sd in DataRun:
  for pd in DataSets:
    tag = pd + '_' + sd
    if 'DoubleMuon' in pd and 'Run2016G' in sd: 
        print("sd      = {}".format(sd))
        print("pd      = {}".format(pd))
        print("Old tag = {}".format(tag))
        tag = tag.replace('v1','v2')
        print("New tag = {}".format(tag))

    files = nanoGetSampleFiles(dataDirectory,tag)

    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))
    addSampleWeight(samples, 'DATA', tag, DataTrig[pd])

###########################################
#############  EFT SIGNALS  ###############
###########################################

############################################################################################################################################################################

#samples = {k:v for k,v in samples.items() if 'sm' not in k and 'lin' not in k and 'quad' not in k} # SM ONLY
samples = {k:v for k,v in samples.items()} # SM + EFT
