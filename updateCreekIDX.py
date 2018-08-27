
# coding: utf-8

# In[102]:


import pandas as pd
import numpy as np

xl = pd.ExcelFile('/home/sean/Nutstore/DY强弱记录(2018).xlsm')
f = pd.HDFStore('./data/creekIDX.hdf5')

#symbols = ['PM', 'WH', 'CF', 'SR', 'PTA', 'OI', 'RI', 'ME', 'FG', 'RS', 'RM', 'ZC', 'JR', 'LR', 'SM', 'CY', 'AP']
#months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


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

headers = ['Date_time', 'st_dn','sw_dn','tr_dn','st','sw','tr','total','st_pct','sw_pct','tr_pct','tt_pct','position']

symbols = xl.sheet_names
symbols.remove("Date")


# In[103]:

for symbol in symbols:
    df = pd.read_excel(xl, sheet_name=symbol, names=headers)
    df.drop(df.index[0], inplace=True)
    df = df.astype(dtype=dtypes)
    df.to_hdf(f, '/'+symbol, format='table', append=True, data_columns=True, mode='a')


#dfa = pd.read_excel('/home/sean/Nutstore/DY强弱记录(2018).xlsm', sheet_name=symbol, names=headers)#,  dtype=dtypes) #, usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12]
#dfa.drop(dfa.index[0], inplace=True)
#dfa = dfa.astype(dtype=dtypes)
#dfa.to_hdf(f, '/' + symbol, format='table', append=True, data_columns=True, mode='a')

f.flush()
f.close()

