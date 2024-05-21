mcProduction = 'Summer20UL18_106x_nAODv9_Full2018v9'
dataReco = 'Run2018_UL2018_nAODv9_Full2018v9'
mcSteps = 'MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9'
fakeSteps = 'DATAl1loose2018v9__l2loose__fakeW'
dataSteps = 'DATAl1loose2018v9__l2loose__l2tightOR2018v9'

treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
treeBaseDir2 = '/eos/user/c/ccarriva/postproc/test/'
#limitFiles = -1

def makeMCDirectory(var=''):
    if var== '':
        return os.path.join(treeBaseDir, mcProduction, mcSteps)
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps + '__' + var)

def makeMCDirectory2(var=''):
    if var== '':
        return os.path.join(treeBaseDir2, mcProduction, mcSteps)
    else:
        return os.path.join(treeBaseDir2, mcProduction, mcSteps + '__' + var)

bsm = ['sm_lin_quad_cW', 'quad_cW','sm_lin_quad_cHW', 'quad_cHW','sm_lin_quad_cHWB', 'quad_cHWB','sm_lin_quad_cHDD', 'quad_cHDD','sm_lin_quad_cHbox', 'quad_cHbox']

# ridefinisci per path locale

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
#cuts2j_em = list(filter(lambda k: k.endswith('ee'), cuts2j))
#cuts2j_mm = list(filter(lambda k: k.endswith('mm'), cuts2j))

nuisances = {}

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.015') for skey in mc if skey not in ['Top', 'DY']) # 'WW'
}

nuisances['lumi_correlated'] = {
    'name': 'lumi_13TeV_correlated',
    'type': 'lnN',
    'samples': dict((skey, '1.009') for skey in mc if skey not in ['Top', 'DY']) # 'WW'
}

nuisances['lumi_correlated_1718'] = {
    'name': 'lumi_13TeV_correlated_1718',
    'type': 'lnN',
    'samples': dict((skey, '1.006') for skey in mc if skey not in  ['Top', 'DY']) # 'WW'
}


#### FAKES
nuisances['fake_syst'] = {
    'name': 'CMS_fake_syst_em',
    'type': 'lnN',
    'samples': {
        'Fake_lep': '1.3'
    },
   #'group': 'fake',
}

nuisances['fake_ele'] = {
    'name': 'CMS_fake_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake_lep': ['fakeWEleUp', 'fakeWEleDown'],
    },
   #'group': 'fake',
#    'AsLnN': '1'
}

nuisances['fake_ele_stat'] = {
    'name': 'CMS_fake_stat_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake_lep': ['fakeWStatEleUp', 'fakeWStatEleDown']
    },
   #'group': 'fake',
#    'AsLnN': '1'
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake_lep': ['fakeWMuUp', 'fakeWMuDown'],
    },
   #'group': 'fake',
#    'AsLnN': '1'
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake_lep': ['fakeWStatMuUp', 'fakeWStatMuDown'],
    },
   #'group': 'fake',
#    'AsLnN': '1'
}

### B-tagger
# Fixed BTV SF variations
'''
for flavour in ['bc', 'light']:
    for corr in ['uncorrelated', 'correlated']:
        btag_syst = [f'btagSF{flavour}_up_{corr}/btagSF{flavour}', f'btagSF{flavour}_down_{corr}/btagSF{flavour}']
        if corr == 'correlated':
            name = f'CMS_btagSF{flavour}_{corr}'
        else:
            name = f'CMS_btagSF{flavour}_2018'
        nuisances[f'btagSF{flavour}{corr}'] = {
            'name': name,
            'skipCMS' : 1,
            'kind': 'weight',
            'type': 'shape',
            'samples': dict((skey, btag_syst) for skey in mc),
        }
'''
for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2018'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'skipCMS' : 1,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    }

##### Trigger Efficiency
#trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)','(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']
trig_syst = ['TriggerSFWeight_2l_u/TriggerSFWeight_2l', 'TriggerSFWeight_2l_d/TriggerSFWeight_2l']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2018',
    'skipCMS' : 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc)
}

##### Electron Efficiency and energy scale

nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2018',
    'skipCMS' : 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc)
}

### first bsm

nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2018',
    'skipCMS' : 1,
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in bsm),
    'folderUp': makeMCDirectory('ElepTup_suffix'),
    'folderDown': makeMCDirectory('ElepTdo_suffix'),
    'AsLnN': '0'
}
'''
nuisances['electronpt_bsm'] = {
    'name': 'CMS_scale_e_2018_bsm',
    'skipCMS' : 1,
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1', '1']) for skey in bsm),
    'folderUp': makeMCDirectory2('ElepTup_suffix'),
    'folderDown': makeMCDirectory2('ElepTdo_suffix'),
    'AsLnN': '0'
}
'''
##### Muon Efficiency and energy scale

nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2018',
    'skipCMS' : 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc)
}

### second bsm

nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2018',
    'skipCMS' : 1,
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in bsm),
    'folderUp': makeMCDirectory('MupTup_suffix'),
    'folderDown': makeMCDirectory('MupTdo_suffix'),
    'AsLnN': '0'
}
'''
nuisances['muonpt_bsm'] = {
    'name': 'CMS_scale_m_2018_bsm',
    'skipCMS' : 1,
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1', '1']) for skey in bsm),
    'folderUp': makeMCDirectory2('MupTup_suffix'),
    'folderDown': makeMCDirectory2('MupTdo_suffix'),
    'AsLnN': '0'
}
'''
### PU ID SF uncertainty
puid_syst = ['Jet_PUIDSF_up/Jet_PUIDSF', 'Jet_PUIDSF_down/Jet_PUIDSF']

nuisances['jetPUID'] = {
    'name': 'CMS_PUID_2018',
    'skipCMS' : 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, puid_syst) for skey in mc)
}
'''
##### Jet energy scale

jes_systs = 
['JESAbsolute','JESAbsolute_2018','JESBBEC1','JESBBEC1_2018','JESEC2','JESEC2_2018','JESFlavorQCD','JESHF','JESHF_2018','JESRelativeBal','JESRelativeSample_2018']

for js in jes_systs:
    # Split source, applied to jets and MET
    nuisances[js] = {
        'name': 'CMS_scale_'+js,
        'skipCMS' : 1,
        'kind': 'suffix',
        'type': 'shape',
        'mapUp': js+'up',
        'mapDown': js+'do',
        'samples': dict((skey, ['1', '1']) for skey in mc),
        'folderUp': makeMCDirectory('RDF__JESup_suffix'),
        'folderDown': makeMCDirectory('RDF__JESdo_suffix'),
        'AsLnN': '0'
    }
'''
##### MET energy scale
nuisances['met'] = {
    'name': 'CMS_scale_met_2018',
    'skipCMS' : 1,
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'METup',
    'mapDown': 'METdo',
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in bsm),
    'folderUp': makeMCDirectory('METup_suffix'),
    'folderDown': makeMCDirectory('METdo_suffix'),
    'AsLnN': '0'
}

### third bsm
'''
nuisances['met_bsm'] = {
    'name': 'CMS_scale_met_2018_bsm',
    'skipCMS' : 1,
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'METup',
    'mapDown': 'METdo',
    'samples': dict((skey, ['1', '1']) for skey in bsm),
    'folderUp': makeMCDirectory2('METup_suffix'),
    'folderDown': makeMCDirectory2('METdo_suffix'),
    'AsLnN': '0'
}
'''
##### Jet energy resolution
#nuisances['JER'] = {
#    'name': 'CMS_res_j_2018',
#    'skipCMS' : 1,
#    'kind': 'suffix',
#    'type': 'shape',
#    'mapUp': 'JERup',
#    'mapDown': 'JERdo',
#    'samples': dict((skey, ['1', '1']) for skey in mc),
#    'folderUp': makeMCDirectory('JERup_suffix'),
#    'folderDown': makeMCDirectory('JERdo_suffix'),
#    'AsLnN': '0'
#}

##### Pileup

nuisances['PU'] = {
    'name': 'CMS_PU_2018',
    'skipCMS' : 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Top'               : ['puWeightUp/puWeight','puWeightDown/puWeight'],
        'DY'                : ['puWeightUp/puWeight','puWeightDown/puWeight'],
#       'WWjj_QCD'          : ['puWeightUp/puWeight','puWeightDown/puWeight'],
#       'WW'                : ['puWeightUp/puWeight','puWeightDown/puWeight'],
#       'WWewk_TL'          : ['puWeightUp/puWeight','puWeightDown/puWeight'],
    },
    'AsLnN': '0',
}

##### PS

nuisances['PS_ISR']  = {
    'name'    : 'PS_ISR',
    'kind'    : 'weight',
    'type'    : 'shape',
    'samples' : dict((skey, ['PSWeight[2]', 'PSWeight[0]']) for skey in mc if 'WWewk' not in skey), #???
    'AsLnN'   : '0',
}

nuisances['PS_FSR']  = {
    'name'    : 'PS_FSR',
    'kind'    : 'weight',
    'type'    : 'shape',
    'samples' : dict((skey, ['PSWeight[3]', 'PSWeight[1]']) for skey in mc if 'WWewk' not in skey), #???
    'AsLnN'   : '0',
}

# QCD scale uncertainty missing

## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '10',
    'includeSignal': '0',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {}
}
