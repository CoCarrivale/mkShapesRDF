import os, glob

##############################################
###### Tree base directory for the site ######
##############################################

limitFiles = -1

mcProduction = 'Summer20UL18_106x_nAODv9_Full2018v9'
dataReco = 'Run2018_UL2018_nAODv9_Full2018v9'
mcSteps = 'MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9'
fakeSteps = 'DATAl1loose2018v9__l2loose__fakeW'
dataSteps = 'DATAl1loose2018v9__l2loose__l2tightOR2018v9'
treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
MCDir = os.path.join(treeBaseDir,  mcProduction , mcSteps)
fakeDirectory = os.path.join(treeBaseDir, dataReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)
chargeFlipDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9'
directory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9'

mcDirectory = MCDir

samples = {}

#from mkShapesRDF.shapeAnalysis.libs.SearchFiles import SearchFiles
from mkShapesRDF.lib.search_files import SearchFiles
searchFiles = SearchFiles()

useXROOTD = False
redirector = ""

def nanoGetSampleFiles(path, name):
    #_files = s.searchFiles(path,  f"/nanoLatino_{name}__part*.root", useXROOTD, redirector=redirector)
    _files = searchFiles.searchFiles(path, name, redirector=redirector)
    #_files = glob.glob(path + f"/nanoLatino_{name}__part*.root")
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

#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include btag weights
mcCommonWeightNoMatch = 'XSWeight*SFweight_mod'
mcCommonWeight = 'XSWeight*SFweight_mod*PromptGenLepMatch4l'

Nlep='4'

eleWP = 'mvaFall17V1Iso_WP90_SS'
muWP  = 'cut_Tight_HWWW'

LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight      = 'XSWeight'
SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut
PromptGenLepMatch   = 'PromptGenLepMatch'+Nlep+'l'
PromptGenLepMatch3l   = 'PromptGenLepMatch3l'
PromptGenLepMatch4l   = 'PromptGenLepMatch4l'


###########################################
#############  BACKGROUNDS  ###############
###########################################

###### DY #######

#files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK')
#samples['SSWW'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 4
#}

#files = nanoGetSampleFiles(mcDirectory, 'WLLJJ_WToLNu_EWK')
#samples['WZ_EWK'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 4
#}

#files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_QCD')
#samples['WpWp_QCD'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 4
#}

### WZ QCD
# files = nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_0Jet') + \
#         nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_1Jet') + \
#         nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_3Jet') + \
#         nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_0Jet') + \
#         nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_2Jet') + \
#         nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_3Jet')
# samples['WZ_QCD'] = {
#     'name': files,
#     'weight': mcCommonWeight+'*1.2',
#     'FilesPerJob': 4
# }

files = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu')
samples['WZ_QCD'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}


samples['ZZ'] = {  'name'  :   nanoGetSampleFiles(directory,'ZZTo2L2Nu')
                             + nanoGetSampleFiles(directory,'ZZTo2Q2L_mllmin4p0')
                             + nanoGetSampleFiles(directory,'ZZTo4L'),
                             #+ nanoGetSampleFiles(directory,'ggZZ4m')
                             #+ nanoGetSampleFiles(directory,'ggZZ4m_ext1')
                             #+ nanoGetSampleFiles(directory,'ggZZ4t')
                             #+ nanoGetSampleFiles(directory,'ggZZ2e2t')
                             #+ nanoGetSampleFiles(directory,'ggZZ2m2t')
                             #+ nanoGetSampleFiles(directory,'ggZZ2e2m'),
                    'weight' :  XSWeight+'*((nLepton==2)*PromptGenLepMatch2l + (nLepton==3)*PromptGenLepMatch3l + (nLepton>3)*PromptGenLepMatch4l)*'+METFilter_MC, #SFweight off
                    'FilesPerJob' : 3,
                 }

#ZZ2LbaseW   = getBaseWnAOD(directory,'Summer20UL18_106x_nAODv9_Full2018v9',['ZZTo2L2Nu_ext1','ZZTo2L2Nu_ext2'])
#ZZ4LbaseW   = getBaseWnAOD(directory,'Summer20UL18_106x_nAODv9_Full2018v9',['ZZTo4L_ext1',   'ZZTo4L_ext2'])
#ggZZbaseW   = getBaseWnAOD(directory,'Summer20UL18_106x_nAODv9_Full2018v9',['ggZZ4m',        'ggZZ4m_ext1'])

#addSampleWeight(samples,'ZZ','ZZTo2L2Nu_ext1',"1.07*"+ZZ2LbaseW+"/baseW") ## The non-ggZZ NNLO/NLO k-factor, cited from https://arxiv.org/abs/1405.2219v1 
#addSampleWeight(samples,'ZZ','ZZTo2L2Nu_ext2',"1.07*"+ZZ2LbaseW+"/baseW") 
#addSampleWeight(samples,'ZZ','ZZTo2L2Q',      "1.07") 
#addSampleWeight(samples,'ZZ','ZZTo4L_ext1',   "1.07*"+ZZ4LbaseW+"/baseW")
#addSampleWeight(samples,'ZZ','ZZTo4L_ext2',   "1.07*"+ZZ4LbaseW+"/baseW") 
#addSampleWeight(samples,'ZZ','ggZZ2e2t',      "1.68") ## The NLO/LO k-factor, cited from https://arxiv.org/abs/1509.06734v1
#addSampleWeight(samples,'ZZ','ggZZ2m2t',      "1.68")
#addSampleWeight(samples,'ZZ','ggZZ2e2m',      "1.68")
#addSampleWeight(samples,'ZZ','ggZZ4m',        "1.68*"+ggZZbaseW+"/baseW")
#addSampleWeight(samples,'ZZ','ggZZ4m_ext1',   "1.68*"+ggZZbaseW+"/baseW")
#addSampleWeight(samples,'ZZ','ggZZ4t',        "1.68")

files = nanoGetSampleFiles(mcDirectory, 'TTZToLLNuNu_M-10') + \
        nanoGetSampleFiles(mcDirectory, 'TTWJetsToLNu')
samples['TTV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
files = nanoGetSampleFiles(mcDirectory, 'tZq_ll')
samples['tZq'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
### Vg
# need: 
# LLAJJ_EWK_MLL-50_MJJ-120_TuneCP5_13TeV-madgraph-pythia8
# LNuAJJ_EWK_MJJ-120_TuneCP5_13TeV-madgraph-pythia8
# old: WGJJ Zg
files = nanoGetSampleFiles(mcDirectory, 'ZGToLLG') #+ \
        #nanoGetSampleFiles(mcDirectory, 'WGJJ')
samples['Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*!(Gen_ZGstar_mass > 0)',
    'FilesPerJob': 10
}
#addSampleWeight(samples, 'Vg', 'Zg', '0.448')

files = nanoGetSampleFiles(mcDirectory, 'ZGToLLG') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin0p1')
        #nanoGetSampleFiles(mcDirectory, 'WGJJ') + \
        #nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')
samples['VgS1'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'FilesPerJob': 4,
    'subsamples': {
        'L': 'gstarLow',
        'H': 'gstarHigh'
    }
}
#addSampleWeight(samples, 'VgS1', 'WGJJ', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS1', 'ZGToLLG', '(Gen_ZGstar_mass > 0)')
addSampleWeight(samples, 'VgS1', 'WZTo3LNu_mllmin0p1', '(Gen_ZGstar_mass > 0.1 && Gen_ZGstar_mass<4)')

### Wrong-sign
files = nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENEN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENMN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENTN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNEN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNMN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNTN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNEN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNMN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNTN')
samples['WW'] = {
    'name': files,
    'weight': 'mcCommonWeight_os',
    'FilesPerJob': 17,
}

files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_top') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop')
samples['Top'] = {
    'name': files,
    'weight': 'mcCommonWeight_os',
    'FilesPerJob': 3,
}

ptllDYW_NLO = '(0.87*(gen_ptll<10)+(0.379119+0.099744*gen_ptll-0.00487351*gen_ptll**2+9.19509e-05*gen_ptll**3-6.0212e-07*gen_ptll**4)*(gen_ptll>=10 && gen_ptll<45)+(9.12137e-01+1.11957e-04*gen_ptll-3.15325e-06*gen_ptll**2-4.29708e-09*gen_ptll**3+3.35791e-11*gen_ptll**4)*(gen_ptll>=45 && gen_ptll<200) + 1*(gen_ptll>200))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'
files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO')
samples['DY'] = {
    'name': files,
    'weight':  'mcCommonWeight_os*( !(Sum(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
        Sum(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )',
    'FilesPerJob': 3,
}

files = nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluHToTauTau_M125') + \
        nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125') + \
        nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125') + \
        nanoGetSampleFiles(mcDirectory, 'ttHToNonbb_M125')
samples['Higgs'] = {
    'name': files,
    'weight': 'mcCommonWeight_os',
    'FilesPerJob': 17,
}
# Others
#files = nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu_DoubleScattering')
#samples['DPS'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 4
#}

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWW') + \
        nanoGetSampleFiles(mcDirectory, 'WWG') 
samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

###########################################
################## FAKE ###################
###########################################

samples['Fake_lep']={'name': [ ] ,
                       'weight' :METFilter_DATA,
                       #'weight': 'METFilter_DATA*fakeW',
                       'weights' : [ ] ,
                       'isData': ['all'],
                       'FilesPerJob' : 20 ,
                     }

###########################################
################## DATA ###################
###########################################

samples['DATA']  = {   'name': [ ] ,
                       'weight' :METFilter_DATA,# + '*' + LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 20 ,
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
    samples['Fake_lep']['name'].extend(files)
    addSampleWeight(samples, 'Fake_lep', datatag, DataTrig[pd])
    #samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))
