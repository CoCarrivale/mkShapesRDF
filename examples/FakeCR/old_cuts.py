# cuts
cuts = {}
# ----------------------------------
# Jet and MET VBS-like selections
preselections = 'MET_pt > 30 && Alt(CleanJet_pt,0,-9999.) >50 && Alt(CleanJet_pt,1,-9999.) >50 && abs(detajj) > 2.5 && mjj > 500 && mll > 20'

# ----------------------------------
# lepton selections for WW
ww = 'nLepton>1 && Alt(Lepton_pt,0,0.)>25 && Alt(Lepton_pt,1,0.)>20 && Alt(Lepton_pt,2,0.)<10'
zveto ='((abs(Alt(Lepton_pdgId,0,-9999)) * abs(Alt(Lepton_pdgId,1,-9999)) == 11*13) || (abs(mll - 91) > 15))'
#
triple_charge = '(((abs(Alt(Lepton_pdgId,0,-9999))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[0],-9999)==2) \
|| abs(Alt(Lepton_pdgId,0,-9999))==13) && ((abs(Alt(Lepton_pdgId,1,-9999))==11 && \
Alt(Electron_tightCharge,Lepton_electronIdx[1],-9999)==2) || abs(Alt(Lepton_pdgId,1,-9999))==13))'
# zeppenfeld variable
zlep_ww='\
(abs((Alt(Lepton_eta,0,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/abs(detajj)) < 0.75) \
&&(abs((Alt(Lepton_eta,1,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/abs(detajj)) < 0.75)'
# b veto, already defined in aliases, here I just recall the definition
NObVeto = '(Sum(CleanJet_pt < 20. && abs(CleanJet_eta) > 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) < 0.4184) == 0)'

# ----------------------------------
cuts['nonPromptCR']= ww +' && ' +' && '+ NObVeto +' && '+ zlep_ww +' && '+ triple_charge +'&& tauVeto_ww'+' && '+ zveto
