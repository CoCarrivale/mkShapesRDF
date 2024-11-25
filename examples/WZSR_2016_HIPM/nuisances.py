# nuisances
nuisances = {}

# name of samples here must match keys in samples.py

##############################################################################################
################################ EXPERIMENTAL UNCERTAINTIES  #################################

## Lumi ##

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2016',
    'type': 'lnN',
    'samples': dict((skey, '1.010') for skey in mcSM if skey not in ['tVx'])
}

nuisances['lumi_Correlated'] = {
    'name': 'lumi_13TeV_correlated',
    'type': 'lnN',
    'samples': dict((skey, '1.006') for skey in mcSM if skey not in ['tVx'])
}

## Lepton Efficiency and Energy Scales ##

nuisances['eff_e'] = {
    'name': 'eff_e_2016_UL',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mcSM)
}

nuisances['electronpt'] = {
    'name': 'scale_e_2016_UL',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1', '1']) for skey in mcSM),
    'folderUp': makeMCDirectory('ElepTup_suffix'),
    'folderDown': makeMCDirectory('ElepTdo_suffix'),
}

nuisances['eff_m'] = {
    'name': 'eff_m_2016_UL',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mcSM)
}
nuisances['muonpt'] = {
    'name': 'scale_m_2016_UL',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1', '1']) for skey in mcSM),
    'folderUp': makeMCDirectory('MupTup_suffix'),
    'folderDown': makeMCDirectory('MupTdo_suffix'),
}

## Fakes ##

nuisances['fake_syst']  = {
               'name'  : 'fake_syst',
               'type'  : 'lnN',
               'samples'  : {
                   'Fake_lep' : '1.30',
                   },
}

nuisances['fake_ele'] = {
    'name': 'fake_e_2016',
    'kind': 'weight',
    'type': 'shape',
    'AsLnN': '0',
    'samples': {
        'Fake_lep': ['fakeWEleUp', 'fakeWEleDown'],
    }
}

nuisances['fake_ele_stat'] = {
    'name': 'fake_stat_e_2016',
    'kind': 'weight',
    'type': 'shape',
    'AsLnN': '0',
    'samples': {
        'Fake_lep': ['fakeWStatEleUp', 'fakeWStatEleDown']
    }
}

nuisances['fake_mu'] = {
    'name': 'fake_m_2016',
    'kind': 'weight',
    'type': 'shape',
    'AsLnN': '0',
    'samples': {
        'Fake_lep': ['fakeWMuUp', 'fakeWMuDown'],
    }
}

nuisances['fake_mu_stat'] = {
    'name': 'fake_stat_m_2016',
    'kind': 'weight',
    'type': 'shape',
    'AsLnN': '0',
    'samples': {
        'Fake_lep': ['fakeWStatMuUp', 'fakeWStatMuDown'],
    }
}

## Pile Up ##

nuisances['PU']  = {
                'name'  : 'PU_2016_UL',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                    s : ['(puWeightUp/puWeight)',
                         '(puWeightDown/puWeight)'] for s in mcSM}, 
                'AsLnN'      : '1',
}

puid_syst = ['Jet_PUIDSF_up/Jet_PUIDSF', 'Jet_PUIDSF_down/Jet_PUIDSF']

nuisances['jetPUID'] = {
    'name': 'PUID_2018_UL',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, puid_syst) for skey in mcSM)
}

## JER ##

nuisances['JER'] = {
                'name': 'res_j_2016_UL',
                'kind': 'suffix',
                'type': 'shape',
                'mapUp': 'JERup',
                'mapDown': 'JERdo',
                'samples': dict((skey, ['1','1']) for skey in mcSM),
                'folderUp' : makeMCDirectory('JERup_suffix'),
                'folderDown' : makeMCDirectory('JERdo_suffix'),
}

## XS ##

apply_on = {
    'Top': [
        '(topGenPt * antitopGenPt <= 0.) * 1.0816 + (topGenPt * antitopGenPt > 0.)',
        '(topGenPt * antitopGenPt <= 0.) * 0.9184 + (topGenPt * antitopGenPt > 0.)'
    ]
}

nuisances['singleTopToTTbar'] = {
    'name': 'singleTopToTTbar',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': apply_on
}

## MET ##

nuisances['met'] = {
    'name': 'scale_met_2016',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'METup',
    'mapDown': 'METdo',
    'samples': dict((skey, ['1', '1']) for skey in mcSM),
    'folderUp': makeMCDirectory('METup_suffix'),
    'folderDown': makeMCDirectory('METdo_suffix'),
    'AsLnN': '1'
}

##############################################################################################
################################# THEORETICAL UNCERTAINTIES  #################################

## Parton Shower ##

nuisances['PS_ISR']  = {
    'name': 'PS_ISR',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['PSWeight[2]', 'PSWeight[0]']) for skey in mc),
}

nuisances['PS_FSR']  = {
    'name': 'PS_FSR',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['PSWeight[3]', 'PSWeight[1]']) for skey in mc),
}

## Underlying Events ##

nuisances['UE']  = {
                'name'  : 'UE_CP5',
                'skipCMS' : 1,
                'type': 'lnN',
                'samples': dict((skey, '1.015') for skey in mcSM), 
}

## PDF ##

nuisances['pdf_weight'] = {
    'name'  : 'pdf',
    'kind'  : 'weight_envelope',
    'type'  : 'shape',
    'samples' :  { s: [' Alt(LHEPdfWeight,'+str(i)+', 1.)' for i in range(0,103)] for s in mcALL}, #check mc > mcALL
}


## QCD scale ##

for sample in mcSM:
     nuisances['QCDscale_' + sample] = {
                'name'  : 'QCDscale_' + sample,
                'kind': 'weight_envelope',
                'type'  : 'shape',
                'samples'  :  { k:["LHEScaleWeight[0]", "LHEScaleWeight[8]"] for k in mcSM },
        }

variations = [
    'LHEScaleWeight[0]',
    'LHEScaleWeight[1]',
    'LHEScaleWeight[3]',
    'LHEScaleWeight[4]',
    'LHEScaleWeight[6]',
    'LHEScaleWeight[7]'
]


nuisances['QCDscale_WZ'] = {
            'name'  : 'QCDscale_WZ',
            'kind': 'weight_envelope',
            'type'  : 'shape',
            'samples'  :  { k:variations for k in mcBSM },
    }

##############################################################################################
########################################## OTHERS  ###########################################

## Rate Parameters ##

nuisances['norm_WZb']  = {
               'name'  : 'norm_WZb',
               'samples'  : {
                   'tVx' : '1.00',
                   },
               'type'  : 'rateParam',
              }

nuisances['norm_WZQCD']  = {
               'name'  : 'norm_WZQCD',
               'samples'  : {
                   'WZ_QCD' : '1.00',
                   },
               'type'  : 'rateParam',
              }

## Stats ##

autoStats = True
if autoStats:
    nuisances['stat'] = {
        'type': 'auto',
        'maxPoiss': '10',
        'includeSignal': '1',
        'samples': {}
}


##############################################################################################

##############################################################################################

##############################################################################################

##############################################################################################

##############################################################################################

'''

# ------------------- trigger
trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'eff_hwwtrigger_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mcALL)
}

# ------------------- btagging
for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'btag_%s' % shift
    if 'stats' in shift:
        name += '_2016'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mcALL), # FIXME if skey not in ['ggH_htt']),
    }


# ------------------- pileup sf
puid_syst = ['Jet_PUIDSF_up/Jet_PUIDSF', 'Jet_PUIDSF_down/Jet_PUIDSF']

nuisances['jetPUID'] = {
    'name': 'PUID_2016_UL',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, puid_syst) for skey in mcALL) #FIXME  if skey not in ['ggH_htt'])
}


# ------------------- XS
nuisances['TopPtRew'] = {
   'name': 'top_pT_reweighting',   # Theory uncertainty
   'kind': 'weight',
   'type': 'shape',
   'samples': {'Top': ["Top_pTrw*Top_pTrw", "1."]},
   'symmetrize': True
}
'''