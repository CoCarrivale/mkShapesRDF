# cuts
cuts = {}

preselections = 'mll>60 && mll<120 && Lepton_pt[0]>25 && Lepton_pt[1]>13 && (nLepton>=2 && Alt(Lepton_pt,2,0)<10) && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 && bVeto'

supercut='\
nLepton>1'
#((Alt(abs(Lepton_pdgId[0]),-9999)==11 && Alt(Electron_tightCharge[Lepton_electronIdx[0]],-9999)==2) || Alt(abs(Lepton_pdgId[0]),-9999)==13) && ((Alt(abs(Lepton_pdgId[1]),-9999)==11 && Alt(Electron_tightCharge[Lepton_electronIdx[1]],-9999)==2) || Alt(abs(Lepton_pdgId[1]),-9999)==13) && ((Alt(abs(Lepton_pdgId[2]),-9999)==11 && Alt(Electron_tightCharge[Lepton_electronIdx[2]],-9999)==2) || Alt(abs(Lepton_pdgId[2]),-9999)==13) && ((Alt(abs(Lepton_pdgId[3]),-9999)==11 && Alt(Electron_tightCharge[Lepton_electronIdx[3]],-9999)==2) || Alt(abs(Lepton_pdgId[3]),-9999)==13)
triple_charge = '((abs(Alt(Lepton_pdgId[0],-9999))==11 && Alt(Electron_tightCharge[Lepton_electronIdx[0]],-9999)==2) || abs(Alt(Lepton_pdgId[0],-9999))==13) && ((abs(Alt(Lepton_pdgId[1],-9999))==11 && Alt(Electron_tightCharge[Lepton_electronIdx[1]],-9999)==2) || abs(Alt(Lepton_pdgId[1],-9999))==13)'
triple_charge_wz = '((abs(Alt(Lepton_pdgId[0],-9999))==11 && Alt(Electron_tightCharge[Lepton_electronIdx[0]],-9999)==2) || abs(Alt(Lepton_pdgId[0],-9999))==13) && ((abs(Alt(Lepton_pdgId[1],-9999))==11 && Alt(Electron_tightCharge[Lepton_electronIdx[1]],-9999)==2) || abs(Alt(Lepton_pdgId[1],-9999))==13) && ((abs(Alt(Lepton_pdgId[2],-9999))==11 && Alt(Electron_tightCharge[Lepton_electronIdx[2]],-9999)==2) || abs(Alt(Lepton_pdgId[2],-9999))==13)'
triple_charge_zz = '((abs(Alt(Lepton_pdgId[0],-9999))==11 && Alt(Electron_tightCharge[Lepton_electronIdx[0]],-9999)==2) || abs(Alt(Lepton_pdgId[0],-9999))==13) && ((abs(Alt(Lepton_pdgId[1],-9999))==11 && Alt(Electron_tightCharge[Lepton_electronIdx[1]],-9999)==2) || abs(Alt(Lepton_pdgId[1],-9999))==13) && ((abs(Alt(Lepton_pdgId[2],-9999))==11 && Alt(Electron_tightCharge[Lepton_electronIdx[2]],-9999)==2) || abs(Alt(Lepton_pdgId[2],-9999))==13) && ((abs(Alt(Lepton_pdgId[3],-9999))==11 && Alt(Electron_tightCharge[Lepton_electronIdx[3]],-9999)==2) || abs(Alt(Lepton_pdgId[3],-9999))==13)'
#supercut='1'#for test on raw samples

ww = 'Alt(Lepton_pt[0],0.)>25 && Alt(Lepton_pt[1],0.)>20 && Alt(Lepton_pt[2],0.)<10 && Alt(CleanJet_pt[0],-9999.) >50 && Alt(CleanJet_pt[1],-9999.) >50 && mll > 20 && MET_pt > 30 && mjj > 500 && abs(detajj) > 2.5'  # bveto tauveto zveto zlep
#wz = 'nLepton>2 && Alt(Lepton_pt[0],0.)>25 && Alt(Lepton_pt[1],0.)>20 && Alt(Lepton_pt[2],0.)>10 && Alt(Lepton_pt[3],0.)<10 && Alt(CleanJet_pt[0],-9999.) >50 && Alt(CleanJet_pt[1],-9999.) >50 && MET_pt > 30 && mjj > 500 && abs(detajj) > 2.5'    # mlll bveto tauveto anti_zveto zlep_wz
#wzb = 'nLepton>2 && Alt(Lepton_pt[0],0.)>25 && Alt(Lepton_pt[1],0.)>20 && Alt(Lepton_pt[2],0.)>10 && Alt(Lepton_pt[3],0.)<10 && Alt(CleanJet_pt[0],-9999.) >50 && Alt(CleanJet_pt[1],-9999.) >50 && MET_pt > 30 && mjj > 500 && abs(detajj) > 2.5' # mlll btag tauveto zlep_wz anti_zveto
wz = 'nLepton>2 && Alt(Lepton_pt[3],0.)<10 && Alt(CleanJet_pt[0],-9999.) >50 && Alt(CleanJet_pt[1],-9999.) >50 && MET_pt > 30 && mjj > 500 && abs(detajj) > 2.5'    
wz_QCD = 'nLepton>2 && Alt(Lepton_pt[3],0.)<10 && Alt(CleanJet_pt[0],-9999.) >50 && Alt(CleanJet_pt[1],-9999.) >50 && MET_pt > 30 && mjj > 200 && mjj < 500 && abs(detajj) < 2.5'
# mlll bveto tauveto anti_zveto zlep_wz
wzb = 'nLepton>2 && Alt(Lepton_pt[3],0.)<10 && Alt(CleanJet_pt[0],-9999.) >50 && Alt(CleanJet_pt[1],-9999.) >50 && MET_pt > 30 && mjj > 500 && abs(detajj) > 2.5' # mlll btag tauveto zlep_wz anti_zveto
loose_wz = 'nLepton>2 && Alt(Lepton_pt[0],0.)>25 && Alt(Lepton_pt[1],0.)>20 && Alt(Lepton_pt[2],0.)>20 && Alt(Lepton_pt[3],0.)<10 && MET_pt > 30' # zveto mlll bveto tauveto
nonprompt = 'Alt(Lepton_pt[0],0.)>25 && Alt(Lepton_pt[1],0.)>20 && Alt(Lepton_pt[2],0.)<10 && Alt(CleanJet_pt[0],-9999.) >50 && Alt(CleanJet_pt[1],-9999.) >50 && mll > 20 && MET_pt > 30 && mjj > 500 && abs(detajj) > 2.5' # btag tauveto zlep zveto
zz = 'nLepton>3 && Alt(Lepton_pt[0],0.)>25 && Alt(Lepton_pt[1],0.)>20 && Alt(Lepton_pt[2],0.)>10 && Alt(Lepton_pt[3],0.)>10 && Alt(Lepton_pt[4],0.)<10 && Alt(CleanJet_pt[0],-9999.) >50 && Alt(CleanJet_pt[1],-9999.) >50 && mjj > 500 && abs(detajj) > 2.5' #  zlep_zz zveto
loose_zz = 'nLepton>3 && Alt(Lepton_pt[0],0.)>25 && Alt(Lepton_pt[1],0.)>20 && Alt(Lepton_pt[2],0.)>10 && Alt(Lepton_pt[3],0.)>10 && Alt(Lepton_pt[4],0.)<10' # ztag
loose_dijet = 'Alt(Lepton_pt[0],0.)>25 && Alt(Lepton_pt[1],0.)>20 && Alt(Lepton_pt[2],0.)<10 && Alt(CleanJet_pt[0],-9999.) >50 && Alt(CleanJet_pt[1],-9999.) >50 && mll > 20 && MET_pt > 30 && mjj > 500 && !('+ww+')' # zveto tauveto

#signal cuts are used as preselections
bJetTag  = '!(bVeto)'

zveto ='(abs(Alt(Lepton_pdgId[0],-9999)) * abs(Alt(Lepton_pdgId[1],-9999)) != 11*11 || abs(mll - 91) > 15)'
# ztag and mlll
ztag ='Alt(WH3l_mlll,-9999.) > 100 \
&& abs(Alt(Lepton_pdgId[0],-9999) + Alt(Lepton_pdgId[1],-9999) + Alt(Lepton_pdgId[2],-9999)) < 20 \
&& ((abs(mll - 91) < 15 && Alt(Lepton_pdgId[0],-9999) * Alt(Lepton_pdgId[1],-9999) <0) \
|| (abs(mllOneThree - 91) < 15 && Alt(Lepton_pdgId[0],-9999) * Alt(Lepton_pdgId[2],-9999) < 0) \
|| (abs(mllTwoThree - 91) < 15 && Alt(Lepton_pdgId[1],-9999) * Alt(Lepton_pdgId[2],-9999) < 0))'
ztag_zz = 'abs(z0Mass_zh4l-91) < 15 && abs(z1Mass_zh4l-91) < 15 '
ztag_zz_loose = 'abs(z0Mass_zh4l-91) < 30 && abs(z1Mass_zh4l-91) < 30 '

zlep='\
(abs((Alt(Lepton_eta[0],-9999.) - (Alt(CleanJet_eta[0],-9999.)+Alt(CleanJet_eta[1],-9999.))/2)/abs(detajj)) < 0.75) \
&&(abs((Alt(Lepton_eta[1],-9999.) - (Alt(CleanJet_eta[0],-9999.)+Alt(CleanJet_eta[1],-9999.))/2)/abs(detajj)) < 0.75)'

zlep_wz='\
(abs((Alt(Lepton_eta[0],-9999.) - (Alt(CleanJet_eta[0],-9999.)+Alt(CleanJet_eta[1],-9999.))/2)/abs(detajj)) < 1.0) \
&&(abs((Alt(Lepton_eta[1],-9999.) - (Alt(CleanJet_eta[0],-9999.)+Alt(CleanJet_eta[1],-9999.))/2)/abs(detajj)) < 1.0) \
&&(abs((Alt(Lepton_eta[2],-9999.) - (Alt(CleanJet_eta[0],-9999.)+Alt(CleanJet_eta[1],-9999.))/2)/abs(detajj)) < 1.0)'

zlep_zz='\
(abs((Alt(Lepton_eta[0],-9999.) - (Alt(CleanJet_eta[0],-9999.)+Alt(CleanJet_eta[1],-9999.))/2)/abs(detajj)) < 0.75) \
&&(abs((Alt(Lepton_eta[1],-9999.) - (Alt(CleanJet_eta[0],-9999.)+Alt(CleanJet_eta[1],-9999.))/2)/abs(detajj)) < 0.75) \
&&(abs((Alt(Lepton_eta[2],-9999.) - (Alt(CleanJet_eta[0],-9999.)+Alt(CleanJet_eta[1],-9999.))/2)/abs(detajj)) < 0.75) \
&&(abs((Alt(Lepton_eta[3],-9999.) - (Alt(CleanJet_eta[0],-9999.)+Alt(CleanJet_eta[1],-9999.))/2)/abs(detajj)) < 0.75)'
ssww='Alt(Lepton_pdgId[0],-9999) * Alt(Lepton_pdgId[1],-9999) > 0'
osww='Alt(Lepton_pdgId[0],-9999) * Alt(Lepton_pdgId[1],-9999) < 0'


wz_zmass_one_two =  "(( abs(mll - 91) < abs(mllOneThree - 91) ) && ( abs(mll - 91) < abs(mllTwoThree - 91) )  &&  ( Alt(Lepton_pt[0],0.)>25 )  && ( Alt(Lepton_pt[1],0.)>10 ) && ( Alt(Lepton_pt[2],0.)>20 ))"
wz_zmass_two_three =  "(( abs(mllTwoThree - 91) < abs(mllOneThree - 91) ) && ( abs(mllTwoThree - 91) < abs(mll - 91) )  &&  ( Alt(Lepton_pt[1],0.)>25 )  && ( Alt(Lepton_pt[2],0.)>10 ) && ( Alt(Lepton_pt[0],0.)>20 ))"
wz_zmass_one_three =  "(( abs(mllOneThree - 91) < abs(mll - 91) ) && ( abs(mllOneThree - 91) < abs(mllTwoThree - 91) )  &&  ( Alt(Lepton_pt[0],0.)>25 ) && ( Alt(Lepton_pt[2],0.)>10 ) && ( Alt(Lepton_pt[1],0.)>20 ))"

wz_zmass = '(' +  wz_zmass_one_two + " || " + wz_zmass_two_three + " || " + wz_zmass_one_three + ')'

cuts['WZQCD_tri']=  {
    'expr' : wz_QCD +'&&' + wz_zmass +' && bVeto &&'+zlep_wz+'&&'+ztag+'&&'+triple_charge_wz,
    'categories': {
        'eee' : '(abs(Alt(Lepton_pdgId[0],-9999)) * abs(Alt(Lepton_pdgId[1],-9999)) * abs(Alt(Lepton_pdgId[2],-9999)) == 11*11*11 )',
        'mmm' : '(abs(Alt(Lepton_pdgId[0],-9999)) * abs(Alt(Lepton_pdgId[1],-9999)) * abs(Alt(Lepton_pdgId[2],-9999)) == 13*13*13 )',
        'eem' : '(abs(Alt(Lepton_pdgId[0],-9999)) * abs(Alt(Lepton_pdgId[1],-9999)) * abs(Alt(Lepton_pdgId[2],-9999)) == 11*11*13 )',
        'mme' : '(abs(Alt(Lepton_pdgId[0],-9999)) * abs(Alt(Lepton_pdgId[1],-9999)) * abs(Alt(Lepton_pdgId[2],-9999)) == 13*13*11 )',
    }
}




cuts['WZb_tri_tauVeto'] = {
    'expr' : wz + ' && ' + wz_zmass + ' && ' + bJetTag+'&&'+zlep_wz+'&&'+ztag+'&&'+triple_charge_wz+'&& tauVeto_wz',
    'categories': {
          'eee' : '(abs(Alt(Lepton_pdgId[0],-9999)) * abs(Alt(Lepton_pdgId[1],-9999)) * abs(Alt(Lepton_pdgId[2],-9999)) == 11*11*11 )',
          'mmm' : '(abs(Alt(Lepton_pdgId[0],-9999)) * abs(Alt(Lepton_pdgId[1],-9999)) * abs(Alt(Lepton_pdgId[2],-9999)) == 13*13*13 )',
          'eem' : '(abs(Alt(Lepton_pdgId[0],-9999)) * abs(Alt(Lepton_pdgId[1],-9999)) * abs(Alt(Lepton_pdgId[2],-9999)) == 11*11*13 )',
          'mme' : '(abs(Alt(Lepton_pdgId[0],-9999)) * abs(Alt(Lepton_pdgId[1],-9999)) * abs(Alt(Lepton_pdgId[2],-9999)) == 13*13*11 )',
    }
}


