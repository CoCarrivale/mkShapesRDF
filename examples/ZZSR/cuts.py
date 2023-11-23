# cuts
cuts = {}

preselections='nLepton>1'

triple_charge_zz = '((abs(Alt(Lepton_pdgId,0,0))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[0],0)==2) || abs(Alt(Lepton_pdgId,0,0))==13) && ((abs(Alt(Lepton_pdgId,1,0))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[1],0)==2) || abs(Alt(Lepton_pdgId,1,0))==13) && ((abs(Alt(Lepton_pdgId,2,0))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[2],0)==2) || abs(Alt(Lepton_pdgId,2,0))==13) && ((abs(Alt(Lepton_pdgId,3,0))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[3],0)==2) || abs(Alt(Lepton_pdgId,3,0))==13)'

zz = 'nLepton>3 && Alt(Lepton_pt,0,0)>25 && Alt(Lepton_pt,1,0)>20 && Alt(Lepton_pt,2,0)>10 && Alt(Lepton_pt,3,0)>10 && Alt(Lepton_pt,4,0)<10 && Alt(CleanJet_pt,0,0) >50 && Alt(CleanJet_pt,1,0) >50 && mjj > 500 && abs(detajj) > 2.5' #  zlep_zz zveto

ztag_zz = 'abs(z0Mass_zh4l-91) < 15 && abs(z1Mass_zh4l-91) < 15 '

zlep_zz='(abs((Alt(Lepton_eta,0,0) - (Alt(CleanJet_eta,0,0)+Alt(CleanJet_eta,1,0))/2)/abs(detajj)) < 0.75) && (abs((Alt(Lepton_eta,1,0) - (Alt(CleanJet_eta,0,0)+Alt(CleanJet_eta,1,0))/2)/abs(detajj)) < 0.75) && (abs((Alt(Lepton_eta,2,0) - (Alt(CleanJet_eta,0,0)+Alt(CleanJet_eta,1,0))/2)/abs(detajj)) < 0.75) && (abs((Alt(Lepton_eta,3,0) - (Alt(CleanJet_eta,0,0)+Alt(CleanJet_eta,1,0))/2)/abs(detajj)) < 0.75)'



cuts['ZZ_tri'] = {
    'expr' : zz+'&&'+ztag_zz+'&&'+triple_charge_zz+'&&'+zlep_zz,
    'categories' : {
      'inclusive': 'true',
      '0j' : 'zeroJet',
   }
}

     


