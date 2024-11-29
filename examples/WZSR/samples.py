import os, glob
mcProduction = 'Summer20UL18_106x_nAODv9_Full2018v9'
dataReco = 'Run2018_UL2018_nAODv9_Full2018v9'
mcSteps = 'MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9'
fakeSteps = 'DATAl1loose2018v9__l2loose__fakeW'
dataSteps = 'DATAl1loose2018v9__l2loose__l2tightOR2018v9'

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
redirector = 'root://eoscms.cern.ch/'     # SM samples
redirector2 = 'root://eoshome-c.cern.ch/' # EFT samples

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
    ['A','Run2018A-UL2018-v1'],
    ['B','Run2018B-UL2018-v1'],
    ['C','Run2018C-UL2018-v1'],
    ['D','Run2018D-UL2018-v1'],
]

DataSets = ['MuonEG','SingleMuon','EGamma','DoubleMuon']

DataTrig = {
    'MuonEG'         : 'Trigger_ElMu' ,
    'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
    'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
    'EGamma'         : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)' ,
}

################################################
############ BASIC MC WEIGHTS ##################
################################################

Nlep='3'

eleWP = 'mvaFall17V2Iso_WP90_SS_tthmva_70'
muWP  = 'cut_Tight_HWWW_tthmva_80'

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

#files = nanoGetSampleFiles(mcDirectory, 'WLLJJ_WToLNu_EWK_UL')
#samples['sm'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 4
#}

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
        nanoGetSampleFiles(mcDirectory, 'tZq_ll')
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
    datatag = pd + '_' + sd

    if (   ('DoubleMuon' in pd and 'Run2018B' in sd)
        or ('DoubleMuon' in pd and 'Run2018D' in sd)
        or ('SingleMuon' in pd and 'Run2018A' in sd)
        or ('SingleMuon' in pd and 'Run2018B' in sd)
        or ('SingleMuon' in pd and 'Run2018C' in sd)):
        print("sd      = {}".format(sd))
        print("pd      = {}".format(pd))
        print("Old datatag = {}".format(datatag))
        datatag = datatag.replace('v1','v2')
        print("New datatag = {}".format(datatag))
    files = nanoGetSampleFiles(fakeDirectory, datatag)

    samples['Fake_lep']['name'].extend(files)
    addSampleWeight(samples, 'Fake_lep', datatag, DataTrig[pd])

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
    datatag = pd + '_' + sd

    if (   ('DoubleMuon' in pd and 'Run2018B' in sd)
        or ('DoubleMuon' in pd and 'Run2018D' in sd)
        or ('SingleMuon' in pd and 'Run2018A' in sd)
        or ('SingleMuon' in pd and 'Run2018B' in sd)
        or ('SingleMuon' in pd and 'Run2018C' in sd)):
        print("sd      = {}".format(sd))
        print("pd      = {}".format(pd))
        print("Old datatag = {}".format(datatag))
        datatag = datatag.replace('v1','v2')
        print("New datatag = {}".format(datatag))

    files = nanoGetSampleFiles(dataDirectory, datatag)

    samples['DATA']['name'].extend(files)
    addSampleWeight(samples, 'DATA', datatag, DataTrig[pd])

###########################################
#############  EFT SIGNALS  ###############
###########################################

files = nanoGetSampleFiles2('/eos/user/c/ccarriva/postproc/test/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'WZdim6')
samples['sm'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_sm,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles2('/eos/user/c/ccarriva/postproc/test/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'WZdim6')
samples['sm_lin_quad_cW'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_sm_lin_quad_cW,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles2('/eos/user/c/ccarriva/postproc/test/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'WZdim6')
samples['quad_cW'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_quad_cW,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles2('/eos/user/c/ccarriva/postproc/test/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'WZdim6')
samples['sm_lin_quad_cHbox'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_sm_lin_quad_cHbox,
    'FilesPerJob': 4
}


files = nanoGetSampleFiles2('/eos/user/c/ccarriva/postproc/test/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'WZdim6')
samples['quad_cHbox'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_quad_cHbox,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles2('/eos/user/c/ccarriva/postproc/test/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'WZdim6')
samples['sm_lin_quad_cHDD'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_sm_lin_quad_cHDD,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles2('/eos/user/c/ccarriva/postproc/test/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'WZdim6')
samples['quad_cHDD'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_quad_cHDD,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles2('/eos/user/c/ccarriva/postproc/test/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'WZdim6')
samples['sm_lin_quad_cHW'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_sm_lin_quad_cHW,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles2('/eos/user/c/ccarriva/postproc/test/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'WZdim6')
samples['quad_cHW'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_quad_cHW,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles2('/eos/user/c/ccarriva/postproc/test/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'WZdim6')
samples['sm_lin_quad_cHWB'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_sm_lin_quad_cHWB,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles2('/eos/user/c/ccarriva/postproc/test/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'WZdim6')
samples['quad_cHWB'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_quad_cHWB,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles2('/eos/user/c/ccarriva/postproc/test/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'WZdim6')
samples['sm_lin_quad_mixed_cW_cHbox'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_sm_lin_quad_mixed_cW_cHbox,
    'FilesPerJob': 4
}

############################################################################################################################################################################

#samples = {k:v for k,v in samples.items() if 'sm' not in k and 'lin' not in k and 'quad' not in k} # SM ONLY
samples = {k:v for k,v in samples.items()} # SM + EFT