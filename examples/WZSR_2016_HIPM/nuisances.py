# nuisances
# S.D. = Susan Dittmer's cfg https://github.com/latinos/PlotsConfigurations/blob/40d4ef1db7d96aea22acfc863d64b83966c12d32/Configurations/WW/FullRunII/Full2016_v9/inclusive/nuisances.py

nuisances = {}

# name of samples here must match keys in samples.py

##############################################################################################
################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity
# ------------------- lumi

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2016',
    'type': 'lnN',
    'samples': dict((skey, '1.010') for skey in mcALL if skey not in ['tVx'])
}

nuisances['lumi_Correlated'] = {
    'name': 'lumi_13TeV_correlated',
    'type': 'lnN',
    'samples': dict((skey, '1.006') for skey in mcALL if skey not in ['tVx'])
}

# ------------------- trigger
trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'eff_hwwtrigger_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mcALL)
}

# ------------------- fakes
nuisances['fake_syst']  = {
               'name'  : 'fake_syst',
               'type'  : 'lnN',
               'samples'  : {
                   'Fake_lep' : '1.30',
                   },
}

#nuisances['fake_syst_em'] = {
#    'name': 'CMS_fake_syst_em',
#    'type': 'lnN',
#    'samples': {
#    'Fake_lep_em': '1.3'
#    },
#}
#
#nuisances['fake_syst_me'] = {
#    'name': 'CMS_fake_syst_me',
#    'type': 'lnN',
#    'samples': {
#    'Fake_lep_me': '1.3'
#    },
#}

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

# ------------------- electron efficiency and energy scale
nuisances['eff_e'] = {
    'name': 'eff_e_2016_UL',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mcALL) # FIXME maybe problems with ggH_htt
}
nuisances['electronpt'] = {
    'name': 'scale_e_2016_UL',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1', '1']) for skey in mcALL), # FIXME if skey not in ['ggH_htt']),
    'folderUp': makeMCDirectory('ElepTup_suffix'),
    'folderDown': makeMCDirectory('ElepTdo_suffix'),
}


# ------------------- muon efficiency and energy scale
nuisances['eff_m'] = {
    'name': 'eff_m_2016_UL',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mcALL), #FIXME  if skey not in ['ggH_htt'])
}
nuisances['muonpt'] = {
    'name': 'scale_m_2016_UL',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1', '1']) for skey in mcALL), #FIXME if skey not in ['ggH_htt']),
    'folderUp': makeMCDirectory('MupTup_suffix'),
    'folderDown': makeMCDirectory('MupTdo_suffix'),
}

# ------------------- JER
nuisances['JER'] = {
                'name': 'res_j_2016_UL',
                'kind': 'suffix',
                'type': 'shape',
                'mapUp': 'JERup',
                'mapDown': 'JERdo',
                'samples': dict((skey, ['1','1']) for skey in mcALL if skey not in ['tVx']),# FIXME if skey not in ['ggH_htt']),
                'folderUp' : makeMCDirectory('JERup_suffix'),
                'folderDown' : makeMCDirectory('JERdo_suffix'),
}

# ------------------- JES
# ----- from Susan's cfg # FIXME this was commented
jes_systs = ['JESAbsolute','JESAbsolute_2016','JESBBEC1','JESBBEC1_2016','JESEC2','JESEC2_2016','JESFlavorQCD','JESHF','JESHF_2016','JESRelativeBal','JESRelativeSample_2016']

for js in jes_systs:
    nuisances[js] = {
        'name': 'scale_'+js,
        'kind': 'suffix',
        'type': 'shape',
        'mapUp': js+'up',
        'mapDown': js+'do',
        'samples': dict((skey, ['1', '1']) for skey in mcSM if skey not in ['SSWW', 'WZ_EWK', 'WpWp_QCD', 'tVx']), # FIXME should be mc
        'folderUp': makeMCDirectory('RDF__JESup_suffix'),
        'folderDown': makeMCDirectory('RDF__JESdo_suffix'),
        'reweight' : ['btagSF'+js.replace('JES','jes')+'up/btagSF','btagSF'+js.replace('JES','jes')+'down/btagSF'],
        'AsLnN': '0'
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

# ------------------- pile up
nuisances['PU']  = {
                'name'  : 'PU_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                    s : ['(puWeightUp/puWeight)',
                         '(puWeightDown/puWeight)'] for s in mcALL}, #FIXME if s not in ['ggH_htt']},
}

# ------------------- pileup sf
puid_syst = ['Jet_PUIDSF_up/Jet_PUIDSF', 'Jet_PUIDSF_down/Jet_PUIDSF']

nuisances['jetPUID'] = {
    'name': 'PUID_2016_UL',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, puid_syst) for skey in mcALL) #FIXME  if skey not in ['ggH_htt'])
}

# ------------------- parton shower (ISR,FSR)
nuisances['PS_ISR']  = {
    'name': 'PS_ISR',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['PSWeight[2]', 'PSWeight[0]']) for skey in mcALL), #FIXME if skey not in ['ggH_htt']),
}

nuisances['PS_FSR']  = {
    'name': 'PS_FSR',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['PSWeight[3]', 'PSWeight[1]']) for skey in mcALL),# FIXME if skey not in ['ggH_htt']),
}

# ------------------- Underlying Event (from S.D.)
nuisances['UE']  = {
                'name'  : 'UE_CP5',
                'skipCMS' : 1,
                'type': 'lnN',
                'samples': dict((skey, '1.015') for skey in mcALL) # FIXME if skey not in ['WW','WW']), 
}

# ------------------- XS
nuisances['TopPtRew'] = {
   'name': 'top_pT_reweighting',   # Theory uncertainty
   'kind': 'weight',
   'type': 'shape',
   'samples': {'Top': ["Top_pTrw*Top_pTrw", "1."]},
   'symmetrize': True
}



# ------------------- PDF
nuisances['pdf_weight'] = {
    'name'  : 'pdf',
    'kind'  : 'weight_envelope',
    'type'  : 'shape',
    'samples' :  { s: [' Alt(LHEPdfWeight,'+str(i)+', 1.)' for i in range(0,103)] for s in mcALL}, 
}

# ------------------- QCD scale
variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[nLHEScaleWeight-4]', 'LHEScaleWeight[nLHEScaleWeight-2]', 'LHEScaleWeight[nLHEScaleWeight-1]']

for sample in mcALL:
    if sample != 'WW':
        nuisances['QCDscale_'+sample] = {
                   'name'  : 'QCDscale_'+sample,
                   'kind': 'weight_envelope',
                   'type'  : 'shape',
                   'samples'  :  { sample: variations },
           }


# ------------------- SSWW pert ord
#nuisances['ssww_pert_ord'] = {
#    'name': 'ssww_pert_ord',
#    'type': 'lnN',
#    'samples': dict((skey, '1.1') for skey in mc if skey in ['SSWW']) 
#}
#
## ------------------- pdf weight
#nuisances['pdf_weight'] = { 
#    'name'  : 'pdf_weight_1718',
#    'kind'  : 'weight_envelope',
#    'type'  : 'shape',
#    'samples' :  { s: [' Alt(LHEPdfWeight,'+str(i)+', 1.)' for i in range(0,103)] for s in mc if s not in ['DPS']}, # if s not in ['DPS']}, # hoping DPS is now fixed
#    'AsLnN':  '1'
#}
##nuisances['pdf_weight_accept'] = {
##     'name'  : 'pdf_weight_1718_accept',
##     'kind'  : 'weight_envelope',
##     'type'  : 'shape',
##     'samples': { k : [ 'Alt(PDFweight_normalized,'+str(i)+', 1.)' for i in range(0,103) ] for k in ['SSWW', 'WZ_EWK']}
## }
#
## ------------------- QCD scale
#nuisances['QCD_scale_accept'] = {
#            'name'  : 'QCDscale_QCD_WW_accept',
#            'kind'  : 'weight',
#            'type'  : 'shape',
#            'samples': { k:["LHEScaleWeight[0]", "LHEScaleWeight[8]"] for k in mc }
#        }
#
# ------------------- MET (new, I completely did not have it before)
nuisances['met'] = {
    'name': 'scale_met_2016_UL',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'METup',
    'mapDown': 'METdo',
    'samples': dict((skey, ['1', '1']) for skey in mcALL), #FIXME  if skey not in ['SSWW','WpWp_QCD','WZ_EWK']),
    'folderUp': makeMCDirectory('METup_suffix'),
    'folderDown': makeMCDirectory('METdo_suffix'),
}

# ------------------- rateparams
nuisances['norm_WZb']  = {
               'name'  : 'norm_WZb',
               'samples'  : {
                   'tVx' : '1.00',
                   },
               'type'  : 'rateParam',
              }

# ------------------- stats
autoStats = True
if autoStats:
    nuisances['stat'] = {
        'type': 'auto',
        'maxPoiss': '10',
        'includeSignal': '1',
        'samples': {}
}
# 'maxPoiss' =  Number of threshold events for Poisson modelling
# 'includeSignal' =  Include MC stat nuisances on signal processes (1=True, 0=False)

# -------------------------------


