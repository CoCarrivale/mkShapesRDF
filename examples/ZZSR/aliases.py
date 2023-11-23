import os
import copy
import inspect


configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file

aliases = {}
aliases = OrderedDict()

bAlgo = 'DeepB'
bWP = '0.4184'

mc     = [skey for skey in samples if skey not in ('Fake_lep', 'DATA')]
SSsamples = [skey for skey in samples if skey not in ('WW','Top','DY','Higgs')]

eleWP = 'mvaFall17V1Iso_WP90_SS_tthmva_70'
muWP  = 'cut_Tight_HWWW_tthmva_80'


aliases['tauVeto_ww'] = {
    'expr': '(Sum(Tau_pt > 18 && abs(Tau_eta)<2.3 && Tau_decayMode &&sqrt( pow(Tau_eta - Lepton_eta[0], 2) + pow(abs(abs(Tau_phi - Lepton_phi[0])-3.1415)-3.1415, 2) ) >= 0.4 && sqrt( pow(Tau_eta - Lepton_eta[1], 2) + pow(abs(abs(Tau_phi - Lepton_phi[1])-3.1415)-3.1415, 2) ) >= 0.4) == 0)'
}

aliases['tauVeto_wz'] = {
    'expr': '(Sum(Alt(Lepton_pt,0,0)>25 && Alt(Lepton_pt,1,0)>20 && Alt(Lepton_pt,2,0)>20 && Alt(Lepton_pt,3,0)<10 && sqrt( pow(Tau_eta - Alt(Lepton_eta,0,-9999), 2) + pow(abs(abs(Tau_phi - Alt(Lepton_phi,0,-9999.))-3.1415)-3.1415, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt(Lepton_eta,1,-9999.), 2) + pow(abs(abs(Tau_phi - Alt(Lepton_phi,1,-9999))-3.1415)-3.1415, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt(Lepton_eta,2,-9999), 2) + pow(abs(abs(Tau_phi - Alt(Lepton_phi,2,-9999.))-3.1415)-3.1415, 2) ) > 0.4) == 0)'
}

aliases['tauVeto_zz'] = {
    'expr': '(Sum(Alt(Lepton_pt,0,0)>25 && Alt(Lepton_pt,1,0)>20 && Alt(Lepton_pt,2,0)>10 && Alt(Lepton_pt,3,0)>10 && Alt(Lepton_pt,4,0.)<10 && sqrt( pow(Tau_eta - Alt(Lepton_eta,0,-9999.), 2) + pow(abs(abs(Tau_phi - Alt(Lepton_phi,0,-9999))-3.1415)-3.1415, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt(Lepton_eta,1,-9999), 2) + pow(abs(abs(Tau_phi - Alt(Lepton_phi,1,-9999))-3.1415)-3.1415, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt(Lepton_eta,2,-9999), 2) + pow(abs(abs(Tau_phi - Alt(Lepton_phi,2,-9999))-3.1415)-3.1415, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt(Lepton_eta,3,-9999), 2) + pow(abs(abs(Tau_phi - Alt(Lepton_phi,3,-9999.))-3.1415)-3.1415, 2) ) > 0.4) == 0)'
}

aliases['softmuon_veto']={
    'expr':'(Sum(abs(Muon_dxy)<0.02 && abs(Muon_dz)<0.1 && Muon_softId && Muon_pt>5 && abs(Muon_eta)<2.4 && sqrt( pow(Muon_eta - Lepton_eta[0], 2) + pow(abs(abs(Muon_phi - Lepton_phi[0])-3.1415)-3.1415, 2) ) >= 0.4 && sqrt( pow(Muon_eta - Lepton_eta[1], 2) + pow(abs(abs(Muon_phi - Lepton_phi[1])-3.1415)-3.1415, 2) ) >= 0.4)==0)'
}

# fiducial
# print('.L %s/2018/ZZSR/fiducial.cc+' % configurations)
# aliases['fid'] = {
#     'linesToAdd': ['.L %s/2018/ZZSR/fiducial.cc+' % configurations],
#     'class': 'FiducialRegion',
#     'samples': mc,
# }

# chargeflip
#print('.L %s/2018/ZZSR/mischarge_sf.cc+' % configurations)
aliases['chargeflip_w'] = {
    #'linesToAdd': ['.L %s/2018/ZZSR/mischarge_sf.cc+' % configurations],
    #'class': 'misID_sf',
    'expr': '1',
    'samples': mc
}
# chargeflip
# lepton sf
#eleWP = 'mvaFall17V2Iso_WP90_SS'

aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': ['VgS','VgS1','VgS2']
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': ['VgS','VgS1','VgS2']
}
# Fake leptons transfer factor
#aliases['fakeW'] = {
#    #'expr': 'fakeW4l_ele_'+eleWP+'_mu_'+muWP,
#    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_4l',
#    'samples': ['Fake_lep']
#}

# And variations - already divided by central values in formulas !
#aliases['fakeWEleUp'] = {
#    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_4lElUp',
#    'samples': ['Fake_lep']
#}
#aliases['fakeWEleDown'] = {
#    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_4lElDown',
#    'samples': ['Fake_lep']
#}
#aliases['fakeWMuUp'] = {
#    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_4lMuUp',
#    'samples': ['Fake_lep']
#}
#aliases['fakeWMuDown'] = {
#    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_4lMuDown',
#    'samples': ['Fake_lep']
#}
#aliases['fakeWStatEleUp'] = {
#    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_4lstatElUp',
#    'samples': ['Fake_lep']
#}
#aliases['fakeWStatEleDown'] = {
#    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_4lstatElDown',
#    'samples': ['Fake_lep']
#}
#aliases['fakeWStatMuUp'] = {
#    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_4lstatMuUp',
#    'samples': ['Fake_lep']
#}
#aliases['fakeWStatMuDown'] = {
#    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_4lstatMuDown',
#    'samples': ['Fake_lep']
#}
# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt(Lepton_promptgenmatched,0,0)*Alt(Lepton_promptgenmatched,1,0)',
    'samples': mc
}

aliases['PromptGenLepMatch3l'] = {
    'expr': 'Alt(Lepton_promptgenmatched,0,0)*Alt(Lepton_promptgenmatched,1,0)*Alt(Lepton_promptgenmatched,2,0)',
    'samples': mc
}

aliases['PromptGenLepMatch4l'] = {
    'expr': 'Alt(Lepton_promptgenmatched,0,0)*Alt(Lepton_promptgenmatched,1,0)*Alt(Lepton_promptgenmatched,2,0)*Alt(Lepton_promptgenmatched,3,0)',
    'samples': mc
}

# PostProcessing did not create (anti)topGenPt for ST samples with _ext1
lastcopy = (1 << 13)

aliases['isTTbar'] = {
    'expr': 'Sum(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 2' % lastcopy,
    'samples': ['top']
}

aliases['isSingleTop'] = {
    'expr': 'Sum(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 1' % lastcopy,
    'samples': ['top']
}

#aliases['topGenPtOTF'] = {
#    'expr': 'Sum((GenPart_pdgId == 6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
#    'samples': ['top']
#}

#aliases['antitopGenPtOTF'] = {
#    'expr': 'Sum((GenPart_pdgId == -6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
#    'samples': ['top']
#}

aliases['Top_pTrw'] = {
    'expr': 'isTTbar * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPtOTF) * TMath::Exp(0.0615 - 0.0005 * antitopGenPtOTF))) + isSingleTop',
    'samples': ['top']
}

#bjet
# No jet with pt > 30 GeV
aliases['zeroJet'] = {
    'expr': 'Alt(CleanJet_pt,0, 0) < 30.'
}

# ==1 jet with pt > 30 GeV
aliases['oneJet'] = {
    'expr': 'Alt(CleanJet_pt,0, 0) >= 30. && Alt(CleanJet_pt,1, 0) < 30.'
}

# ==2 jets with pt > 30 GeV
aliases['twoJet'] = {
    'expr': 'Alt(CleanJet_pt,0, 0) >= 30. && Alt(CleanJet_pt,1, 0) >= 30. && Alt(CleanJet_pt,2, 0) < 30.'
}

# >=2 jets with pt > 30 GeV
aliases['twoJetOrMore'] = {
    'expr': 'Alt(CleanJet_pt,0, 0) >= 30. && Alt(CleanJet_pt,1, 0) >= 30.'
}


aliases['bVeto'] = {
    'expr': 'Sum(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1241) == 0'
}

aliases['bReq'] = {
    'expr': 'Sum(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1241) >= 1'
}

aliases['btag0'] = {
    'expr': 'zeroJet && !bVeto'
}

aliases['btag1'] = {
    'expr': 'oneJet && bReq'
}

aliases['btag2'] = {
    'expr': 'twoJet && bReq'
}

# lepton eta range
aliases['lep0eta']={
    'expr': '((abs(Alt(Lepton_pdgId,0,-9999))==11 && abs(Alt(Lepton_eta,0,-9999)) <2.5) || (abs(Alt(Lepton_pdgId,0,-9999))==13 && abs(Alt(Lepton_eta,0,-9999)) <2.4))'
}
aliases['lep1eta']={
    'expr': '((abs(Alt(Lepton_pdgId,1,-9999))==11 && abs(Alt(Lepton_eta,1,-9999)) <2.5) || (abs(Alt(Lepton_pdgId,1,-9999))==13 && abs(Alt(Lepton_eta,1,-9999)) <2.4))'
}
aliases['jetpt30']={
    'expr': 'Alt(CleanJet_pt,0,-9999) >30 && Alt(CleanJet_pt,1,-9999) >30'
}
aliases['jetpt50']={
    'expr': 'Alt(CleanJet_pt,0,-9999) >50 && Alt(CleanJet_pt,1,-9999) >50'
}
aliases['leppt0']={
    'expr': 'Alt(Lepton_pt,0,-9999) >25 && Alt(Lepton_pt,1,-9999) >20'
}
aliases['leppt1']={
    'expr': 'Alt(Lepton_pt,0,-9999) >30 && Alt(Lepton_pt,1,-9999) >30'
}
# -3.2<eta<-1.3 and -1.57<phi< -0.87
aliases['HEM']={
    'expr': '(Alt(CleanJet_eta,0,-9999.)>-3.2 && Alt(CleanJet_eta,0,-9999.)<-1.3 && Alt(CleanJet_phi,0,-9999.)>-1.57 && Alt(CleanJet_phi,0,-9999.)<-0.87) || \
        (Alt(CleanJet_eta,1,-9999.)>-3.2 && Alt(CleanJet_eta,1,-9999.)<-1.3 && Alt(CleanJet_phi,1,-9999.)>-1.57 && Alt(CleanJet_phi,1,-9999.)<-0.87)'
}
# ssww region
aliases['zlep_ww']={
    'expr': 'abs((Alt(Lepton_eta,0,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/detajj) < 0.75 && abs((Alt(Lepton_eta,1,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/detajj) < 0.75'
}
aliases['zveto_ww']={
    'expr': '(abs(Alt(Lepton_pdgId,0,-9999)) * abs(Alt(Lepton_pdgId,1,-9999)) != 11*11 || abs(mll - 91.1876) > 15)'
}
#aliases['ssww_region']={
#    'expr': 'nLepton>1 && nCleanJet >1 && Alt(Lepton_pt[2],0.)<10 && MET_pt>30 && mll > 20 && abs(Alt(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt(CleanJet_eta[1],-9999.)) < 4.7 && tauVeto_ww && zveto_ww && lep0eta && lep1eta'  # pt zlep mjj detajj
#}

# B tag scale factors

#btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_102XSF_V1.csv' % os.getenv('CMSSW_BASE')
#
#aliases['Jet_btagSF_shapeFix'] = {
#    'linesToAdd': [
#        'gSystem->Load("libCondFormatsBTauObjects.so");',
#        'gSystem->Load("libCondToolsBTau.so");',
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
#        '.L %s/patches/btagsfpatch.cc+' % configurations
#    ],
#    'class': 'BtagSF',
#    'args': (btagSFSource,),
#    'samples': mc
#}

#aliases['bVetoSF'] = {
#    'expr': 'TMath::Exp(Sum(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
#    'samples': mc
#}

#aliases['btag0SF'] = {
#    'expr': 'TMath::Exp(Sum(TMath::Log((CleanJet_pt>20 && CleanJet_pt<30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || CleanJet_pt>30 || abs(CleanJet_eta)>2.5))))',
#    'samples': mc
#}

#aliases['btagnSF'] = {
#    'expr': 'TMath::Exp(Sum(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx] + (CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
#    'samples': mc
#}

#aliases['btagSF'] = {
#    'expr': 'bVetoSF*bVeto + btag0SF*btag0 + btagnSF*(btag1 + btag2) + (!bVeto && !btag0 && !btag1 && !btag2)',
#    'samples': mc
#}

#for shift in ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:
    #aliases['Jet_btagSF_deepcsv_shape_up_%s' % shift] = {
    #    'class': 'BtagSF',
    #    'args': (btagSFSource, 'up_' + shift),
    #    'samples': mc
    #}
    #aliases['Jet_btagSF_deepcsv_shape_down_%s' % shift] = {
    #    'class': 'BtagSF',
    #    'args': (btagSFSource, 'down_' + shift),
    #    'samples': mc
    #}

#    for targ in ['bVeto', 'btag0', 'btagn']:
#        alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
#        alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_up_%s' % shift)

#        alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
#        alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_down_%s' % shift)

#    aliases['btagSF%sup' % shift] = {
#        'expr': 'bVetoSF{shift}up*bVeto + btag0SF{shift}up*btag0 + btagnSF{shift}up*(btag1 + btag2) + (!bVeto && !btag0 && !btag1 && !btag2)'.format(shift = shift),
#        'samples': mc
#    }

#    aliases['btagSF%sdown' % shift] = {
#        'expr': 'bVetoSF{shift}down*bVeto + btag0SF{shift}down*btag0 + btagnSF{shift}down*(btag1 + btag2) + (!bVeto && !btag0 && !btag1 && !btag2)'.format(shift = shift),
#        'samples': mc
#    }

#aliases['LepWPCut'] = {
#    'expr': 'LepCut4l__ele_'+eleWP+'__mu_'+muWP,
#    'samples': mc + ['DATA']
#}


#data/MC scale factors
aliases['SFweight_mod'] = {
    'expr': ' * '.join(['SFweight3l','METFilter_MC']),#'LepWPCut' 'btagSF']), bveto_sf*lep_sf*trig_sf*mu_roc_sf
    #'expr': 'LepWPCut',
    'samples': mc
}

aliases['mcCommonWeight_os'] = {
    'expr': 'XSWeight*SFweight_mod*PromptGenLepMatch3l*chargeflip_w*(Alt(Lepton_pdgId,0,-9999) * Alt(Lepton_pdgId,1,-9999) < 0)',
    'samples':mc
}

aliases['samesign_requirement'] = {
    'expr': '(Alt(Lepton_pdgId,0,-9999) * Alt(Lepton_pdgId,1,-9999) > 0)',
    'samples':SSsamples
}


# variations
aliases['zlep1'] = {'expr' : '(Alt(Lepton_eta,0,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/detajj'}
aliases['zlep2'] = {'expr' : '(Alt(Lepton_eta,1,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/detajj'}




########################################################################## 
############### my own weights for the nuisances #########################

#aliases['SFweightEleUp'] = {
#    'expr': 'LepSF2l__ele_'+eleWP+'__Up',
#    'samples': mc
#}
#aliases['SFweightEleDown'] = {
#    'expr': 'LepSF2l__ele_'+eleWP+'__Do',
#    'samples': mc
#}
#aliases['SFweightMuUp'] = {
#    'expr': 'LepSF2l__mu_'+muWP+'__Up',
#    'samples': mc
#}
#aliases['SFweightMuDown'] = {
#    'expr': 'LepSF2l__mu_'+muWP+'__Do',
#    'samples': mc
#}



# for shift in ['jes', 'lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
#       for targ in ['bVeto', 'bReq']:
#           alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
#           alias['expr'] = alias['expr'].replace('btagSF_deepcsv_shape', 'btagSF_deepcsv_shape_up_%s' % shift)

#           alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
#           alias['expr'] = alias['expr'].replace('btagSF_deepcsv_shape', 'btagSF_deepcsv_shape_down_%s' % shift)

#       aliases['btagSF%sup' % shift] = {
#           'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
#           'samples': mc
#       }

#       aliases['btagSF%sdown' % shift] = {
#           'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
#           'samples': mc
#       }


#aliases['Jet_PUIDSF'] = {
#  'expr' : 'TMath::Exp(Sum((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose)))',
#  'samples': mc
#}

#aliases['Jet_PUIDSF_up'] = {
#  'expr' : 'TMath::Exp(Sum((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose_up)))',
#  'samples': mc
#}

#aliases['Jet_PUIDSF_down'] = {
#  'expr' : 'TMath::Exp(Sum((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose_down)))',
#  'samples': mc
#}
