import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file

aliases = {}
aliases = OrderedDict()

bAlgo = 'DeepB'
bWP = '0.7527'

eleWP = 'mvaFall17V2Iso_WP90_SS_tthmva_70'
muWP  = 'cut_Tight_HWWW_tthmva_80'

mcBSM     = [skey for skey in samples if 'lin' in skey or 'quad' in skey or 'sm' in skey]
mcEFT     = [skey for skey in samples if 'lin' in skey or 'quad' in skey] 
mcSM      = [skey for skey in samples if skey not in ('DATA', 'Fake_lep') and skey not in mcBSM]
mc        = [skey for skey in samples if skey not in ('DATA', 'Fake_lep') and skey not in mcEFT]
mcALL     = [skey for skey in samples if skey not in ('DATA', 'Fake_lep')]
OSsamples = [skey for skey in mc if skey in ('WW','DY','Higgs','qqH_htt','qqH_hww','ggH_hww','ggH_htt','ttH_hww','Top')]
SSsamples = [skey for skey in samples if skey not in OSsamples] # 'Top' shoud be here

# -------- tau veto

aliases['tauVeto_wz'] = {
    'expr': '(Sum(Alt(Lepton_pt,0,0.)>25 && Alt(Lepton_pt,1,0.)>20 && Alt(Lepton_pt,2,0.)>20 && Alt(Lepton_pt,3,0.)<10 && sqrt( pow(Tau_eta - Alt(Lepton_eta,0,-9999.), 2) + pow(abs(abs(Tau_phi - Alt(Lepton_phi,0,-9999.))-M_PI)-M_PI, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt(Lepton_eta,1,-9999.), 2) + pow(abs(abs(Tau_phi - Alt(Lepton_phi,1,-9999.))-M_PI)-M_PI, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt(Lepton_eta,2,-9999.), 2) + pow(abs(abs(Tau_phi - Alt(Lepton_phi,2,-9999.))-M_PI)-M_PI, 2) ) > 0.4) == 0)'
}

# -------- lepton misidentification SF
aliases['__chargeflip_w'] = {
    'linesToAdd': ['#include "/afs/cern.ch/user/c/ccarriva/mkShapesRDF/examples/WZSR/mischarge_sf.cc"\n'],
    'samples': OSsamples
}
aliases['chargeflip_w'] = {
    'expr' : 'misID_sf(nLepton,Lepton_pdgId,Lepton_pt,Lepton_eta)',
    'samples': OSsamples
}

# -------- weights for VgS1
aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': ['VgS']
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': ['VgS']
}

# -------- gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt(Lepton_promptgenmatched,0,0)*Alt(Lepton_promptgenmatched,1,0)',
    'samples': mcALL
}
aliases['PromptGenLepMatch3l'] = {
     'expr': 'Alt(Lepton_promptgenmatched,0,0)*Alt(Lepton_promptgenmatched,1,0)*Alt(Lepton_promptgenmatched,2,0)',
     'samples': mcALL
 }
aliases['PromptGenLepMatch4l'] = {
    'expr': 'Alt(Lepton_promptgenmatched,0,0)*Alt(Lepton_promptgenmatched,1,0)*Alt(Lepton_promptgenmatched,2,0)*Alt(Lepton_promptgenmatched,3,0)',
    'samples': mcALL
}

# -------- lepton WP
aliases['LepWPCut'] = {
    'expr': 'LepCut3l__ele_'+eleWP+'__mu_'+muWP
}

# -------- top pt
aliases['Top_pTrw'] = {
    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPt) * TMath::Exp(0.0615 - 0.0005 * antitopGenPt))) + (topGenPt * antitopGenPt <= 0.)',
    'samples': ['Top']
}
# -------- fake lepton weights and variations
aliases['fakeW'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3l',
    'samples': ['Fake_lep']
}
aliases['fakeWEleUp'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lElUp',
    'samples': ['Fake_lep']
}
aliases['fakeWEleDown'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lElDown',
    'samples': ['Fake_lep']
}
aliases['fakeWMuUp'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lMuUp',
    'samples': ['Fake_lep']
}
aliases['fakeWMuDown'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lMuDown',
    'samples': ['Fake_lep']
}
aliases['fakeWStatEleUp'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lstatElUp',
    'samples': ['Fake_lep']
}
aliases['fakeWStatEleDown'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lstatElDown',
    'samples': ['Fake_lep']
}
aliases['fakeWStatMuUp'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lstatMuUp',
    'samples': ['Fake_lep']
}
aliases['fakeWStatMuDown'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lstatMuDown',
    'samples': ['Fake_lep']
}

# ---------------------------- btagging (new)
#loose 0.1241
#medium 0.4184
#tight 0.7527
aliases['bVeto'] = {
    'expr': '(Sum(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.7527) == 0)'
}

aliases['bReq'] = {
    'expr': '(Sum(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.7527) >= 1)'
}
aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape,CleanJet_jetIdx)+1*(CleanJet_pt<=20 || abs(CleanJet_eta)>=2.5))))',
    'samples': mcALL
}
aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape,CleanJet_jetIdx)+1*(CleanJet_pt<=30 || abs(CleanJet_eta)>=2.5))))',
    'samples': mcALL
}
aliases['btagSF'] = {
    'expr': 'bVeto*bVetoSF + bReq*bReqSF',
    'samples': mcALL
}


for shift in ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:

    for targ in ['bVeto', 'bReq']:
        alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_deepjet_shape', 'btagSF_deepjet_shape_up_%s' % shift)

        alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_deepjet_shape', 'btagSF_deepjet_shape_down_%s' % shift)

    aliases['btagSF%sup' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
        'samples': mcALL
    }

    aliases['btagSF%sdown' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
        'samples': mcALL
    }


# ---------------------------- SFweight (new)
aliases['SFweight_mod'] = {
    'expr': ' * '.join(['XSWeight',
                        'SFweight3l',
                        'LepSF3l__ele_' + eleWP + '__mu_' + muWP, 
                        'LepWPCut',
                        'METFilter_MC']),
    'samples': mcALL
}

aliases['samesign_requirement'] = {
    'expr': '(Alt(Lepton_pdgId,0,-9999) * Alt(Lepton_pdgId,1,-9999) > 0)',
    'samples':SSsamples
}

aliases['oppositesign_requirement'] = {
    'expr': 'chargeflip_w*(Alt(Lepton_pdgId,0,-9999) * Alt(Lepton_pdgId,1,-9999) < 0)',
    'samples':OSsamples
}

# --------------------------- ele/mu SF weights

aliases['SFweightEleUp'] = {
    'expr': 'LepSF3l__ele_'+eleWP+'__Up',
    'samples': mcALL
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF3l__ele_'+eleWP+'__Do',
    'samples': mcALL
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF3l__mu_'+muWP+'__Up',
    'samples': mcALL
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF3l__mu_'+muWP+'__Do',
    'samples': mcALL
}

# --------------------------- PU weights
aliases['Jet_PUIDSF'] = {
  'expr' : 'TMath::Exp(Sum((Jet_jetId>=2)*LogVec(Jet_PUIDSF_loose)))',
  'samples': mcALL
}

aliases['Jet_PUIDSF_up'] = {
  'expr' : 'TMath::Exp(Sum((Jet_jetId>=2)*LogVec(Jet_PUIDSF_loose_up)))',
  'samples': mcALL
}

aliases['Jet_PUIDSF_down'] = {
  'expr' : 'TMath::Exp(Sum((Jet_jetId>=2)*LogVec(Jet_PUIDSF_loose_down)))',
  'samples': mcALL
}


