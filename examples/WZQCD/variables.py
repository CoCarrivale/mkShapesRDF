# variables

variables = {}

#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

variables['events']  = {   'name': '1',
                           'range' : (1,0,2),
                           'xaxis' : 'events',
                           'fold' : 3
                           }

variables['ptj1']  = {   'name': 'Alt(CleanJet_pt,0,-9999.)',
                           'range' : (15,0.,200),
                           'xaxis' : 'p_{T} 1st jet',
                           'fold'  : 3
                           }

variables['ptj2']  = {   'name': 'Alt(CleanJet_pt,1,-9999.)',
                           'range' : (15,0.,150),
                           'xaxis' : 'p_{T} 2nd jet',
                           'fold'  : 3
                           }
variables['ptl1']  = {   'name': 'Alt(Lepton_pt,0,-9999.)',
                           'range' : (15,0.,200),
                           'xaxis' : 'p_{T} 1st jet',
                           'fold'  : 3
                           }

variables['ptl2']  = {   'name': 'Alt(Lepton_pt,1,-9999.)',
                           'range' : (15,0.,150),
                           'xaxis' : 'p_{T} 2nd jet',
                           'fold'  : 3
                           }

variables['mjj']  = {  'name': 'mjj', # for comparison with paper (ww)
                       'range' : (12,200.,500),
                       'xaxis': 'mjj [GeV]',
                       'fold': 3,
                       }

variables['mll']  = {   'name': 'mll',
                        'range' : (10,20,500),
                        'xaxis' : 'mll [GeV]',
                        'fold' : 3,
                        }

variables['mll_mjj']  = {   'name': 'mll:mjj',
                            'range' : ([500,800,1200,1800,3000],[20,80,140,240,600]),
                            'xaxis' : 'mll:mjj [GeV]',
                            'fold' : 3,
                            'doWeight' : 1,
                            'binX'     : 4,
                            'binY'     : 4
                            }

variables['detajj']  = {    'name': 'detajj',
                            'range': (16,0.0,8.0),
                            'xaxis': 'detajj',
                            'fold': 3,
                            'cuts': ['WZ_tri_tauVeto_incl','WZb_tri_tauVeto_incl','WZQCD_tri_incl'],
                            'blind': { c:[0,8] for c in cuts if "WZ_" in c}
                            }

variables['etaj1'] =    {   'name': 'Alt(Jet_eta,0,-9999.)',
                            'range': (10,-5,5),
                            'xaxis': 'etaj1',
                            'fold': 3
                            }

variables['etaj2'] = {  'name': 'Alt(Jet_eta,1,-9999.)',
                        'range': (10,-5,5),
                        'xaxis': 'etaj2',
                        'fold': 3
                        }

variables['met']  = {   'name': 'MET_pt',            
                        'range' : (10,0,200),       
                        'xaxis' : 'met [GeV]', 
                        'fold' : 3
                        }

variables['Zlep1']  = {  'name': '(Alt(Lepton_eta,0,-9999.) - (Alt(Jet_eta,0,-9999.)+Alt(Jet_eta,1,-9999.))/2)/detajj',
                         'range': (10,-1.5,1.5),
                         'xaxis': 'Z^{lep}_{1}',
                         'fold': 3
                         }

variables['Zlep2']  =   {   'name': '(Alt(Lepton_eta,1,-9999.) - (Alt(Jet_eta,0,-9999.)+Alt(Jet_eta,1,-9999.))/2)/detajj',
                            'range': (10,-1.5,1.5),
                            'xaxis': 'Z^{lep}_{2}',
                            'fold': 3
                            }

variables = {k:v for k,v in variables.items() if k in ['events','ptj1','ptj2','ptl1','ptl2','mjj','mll','mll_mjj','detajj','etaj1','etaj2','met','Zlep1','Zlep2']}