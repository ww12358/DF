# -*- coding:utf-8 -*-

excel_path = '/home/sean/Nutstore/DY强弱记录(2018).xlsm'
h5_path = './data/creekIDX.hdf5'

dtypes = {
        'Date_time':'datetime64[ns]',
        'st_dn' :   'int64',
        'sw_dn' :   'int64',
        'tr_dn' :   'int64',
        'st'    :   'int64',
        'sw'    :   'int64',
        'tr'    :   'int64',
        'total' :   'int64',
        'st_pct':   'float64',
        'sw_pct':   'float64',
        'tr_pct':   'float64',
        'tt_pct':   'float64',
        'position': 'float64'
          }

grp_dtypes = {
        'st_dn' :   'int64',
        'sw_dn' :   'int64',
        'tr_dn' :   'int64',
        'st'    :   'int64',
        'sw'    :   'int64',
        'tr'    :   'int64',
        'total' :   'int64',
        'st_pct':   'float64',
        'sw_pct':   'float64',
        'tr_pct':   'float64',
        'tt_pct':   'float64',
        'position': 'float64'
          }

headers = ['Date_time', 'st_dn','sw_dn','tr_dn','st','sw','tr','total','st_pct','sw_pct','tr_pct','tt_pct','position']


symbol_collection=[
                   'A','M','Y', 'P', 'C', #'JD',
                   'SR', 'CF', 'WH', 'OI', 'RM',  'RS', 'RI',
                   'CU', 'AL', 'ZN', 'PB', 'RU', 'AU', 'AG', 'RB',
                   'TA', 'ME', 'ZC', 'FG',
                   'PP', 'L', 'V', 'I', 'J', 'JM',
                   'IF', 'IH', 'IC', 'TF'
                   ]        #31 symbols

c_idx = ['A', 'M', 'Y', 'P', 'C',
        'SR', 'CF', 'WH', 'OI', 'RM',
        'CU', 'AL', 'ZN', 'PB', 'RU', 'AU', 'AG', 'RB',
        'TA', 'ME', 'ZC',
        'PP', 'L', 'V', 'I', 'J', 'JM']

ferrous = ['RB', 'I', 'J']

nonferous = ['CU', 'AL', 'ZN', 'PB']

construction = ['RB', 'FG', 'V']

coal = ['ZC', 'J', 'JM']

grain = ['C', 'WH', 'A']

feed = ['C', 'WH', 'M', 'RM']

soybean = ['A', 'M', 'Y']

oil = ['Y', 'OI', 'P']

soft = ['SR', 'CF']

chemical = ['PP', 'L', 'TA', 'ME', 'V', 'RU']

industrial = ['CU', 'AL', 'ZN', 'PB', 'RU', 'RB', 'TA', 'ME', 'ZC', 'PP', 'L', 'V', 'I', 'J', 'JM']

algricultural = ['A', 'M', 'Y', 'P', 'C', 'SR', 'CF', 'WH', 'OI', 'RM', ]

equity = ['IF', 'IH', 'IC', 'TF']

symbol_d = {"FER":ferrous, "NON":nonferous, "CON":construction, "COA":coal,
            "GRA":grain, "FEE":feed, "SOY":soybean, "OIL":oil,
            "SOF":soft, "CHE":chemical, "IND":industrial, "EQU":equity,
            "ALG":algricultural
            }