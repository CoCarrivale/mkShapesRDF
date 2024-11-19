# nuisances
nuisances = {}

# name of samples here must match keys in samples.py

##############################################################################################
################################ EXPERIMENTAL UNCERTAINTIES  #################################

## Lumi ##

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.015') for skey in mcSM if skey not in ['tVx'])
}

nuisances['lumi_Correlated'] = {
    'name': 'lumi_13TeV_correlated',
    'type': 'lnN',
    'samples': dict((skey, '1.020') for skey in mcSM if skey not in ['tVx'])
}

nuisances['lumi_1718'] = {
    'name': 'lumi_13TeV_1718',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mcSM if skey not in ['tVx'])
}

## Lepton Efficiency and Energy Scales ##

nuisances['eff_e'] = {
    'name': 'eff_e_2018_UL',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mcSM)
}

nuisances['electronpt'] = {
    'name': 'scale_e_2018_UL',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1', '1']) for skey in mcSM),
    'folderUp': makeMCDirectory('ElepTup_suffix'),
    'folderDown': makeMCDirectory('ElepTdo_suffix'),
}

nuisances['eff_m'] = {
    'name': 'eff_m_2018_UL',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mcSM)
}
nuisances['muonpt'] = {
    'name': 'scale_m_2018_UL',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1', '1']) for skey in mcSM),
    'folderUp': makeMCDirectory('MupTup_suffix'),
    'folderDown': makeMCDirectory('MupTdo_suffix'),
}

## Fakes ##

nuisances['fake_ele'] = {
    'name': 'fake_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'AsLnN': '0',
    'samples': {
        'Fake_lep': ['fakeWEleUp', 'fakeWEleDown'],
    }
}

nuisances['fake_ele_stat'] = {
    'name': 'fake_stat_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'AsLnN': '0',
    'samples': {
        'Fake_lep': ['fakeWStatEleUp', 'fakeWStatEleDown']
    }
}

nuisances['fake_mu'] = {
    'name': 'fake_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'AsLnN': '0',
    'samples': {
        'Fake_lep': ['fakeWMuUp', 'fakeWMuDown'],
    }
}

nuisances['fake_mu_stat'] = {
    'name': 'fake_stat_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'AsLnN': '0',
    'samples': {
        'Fake_lep': ['fakeWStatMuUp', 'fakeWStatMuDown'],
    }
}

## Pile Up ##

nuisances['PU']  = {
                'name'  : 'PU_2018_UL',
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
                'name': 'res_j_2018_UL',
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
    'name': 'scale_met_2018',
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
    'samples' :  { s: [' Alt(LHEPdfWeight,'+str(i)+', 1.)' for i in range(0,103)] for s in mc},
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

## Stats ##

autoStats = True
if autoStats:
    nuisances['stat'] = {
        'type': 'auto',
        'maxPoiss': '10',
        'includeSignal': '1',
        'samples': {}
}


