# cuts
cuts = {}
# ----------------------------------
# Jet and MET VBS-like selections
preselections = 'Alt(CleanJet_pt,0,-9999.) >50 && Alt(CleanJet_pt,1,-9999.) >50 && mll > 20 && MET_pt > 30 && mjj > 500 && abs(detajj) > 2.5'

triple_charge_zz = '((abs(Alt(Lepton_pdgId,0,-9999))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[0],-9999)==2) || abs(Alt(Lepton_pdgId,0,-9999))==13) \
                && ((abs(Alt(Lepton_pdgId,1,-9999))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[1],-9999)==2) || abs(Alt(Lepton_pdgId,1,-9999))==13) \
                && ((abs(Alt(Lepton_pdgId,2,-9999))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[2],-9999)==2) || abs(Alt(Lepton_pdgId,2,-9999))==13) \
                && ((abs(Alt(Lepton_pdgId,3,-9999))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[3],-9999)==2) || abs(Alt(Lepton_pdgId,3,-9999))==13)'

zz = 'nLepton>3 && Alt(Lepton_pt,0,0.)>25 && Alt(Lepton_pt,1,0.)>20 && Alt(Lepton_pt,2,0.)>10 && Alt(Lepton_pt,3,0.)>10 && Alt(Lepton_pt,4,0.)<10'

ztag_zz = 'abs(z0Mass_zh4l-91) < 15 && abs(z1Mass_zh4l-91) < 15 '
zlep_zz='\
(abs((Alt(Lepton_eta,0,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/abs(detajj)) < 1) \
&&(abs((Alt(Lepton_eta,1,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/abs(detajj)) < 1) \
&&(abs((Alt(Lepton_eta,2,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/abs(detajj)) < 1) \
&&(abs((Alt(Lepton_eta,3,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/abs(detajj)) < 1)'

cuts['ZZ']= zz+'&&'+zlep_zz+'&&'+ztag_zz+'&&'+triple_charge_zz

