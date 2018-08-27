# -*- coding:utf-8 -*-
from include import symbol_d, \
                    symbol_collection, \
                    ferrous, nonferous, \
                    industrial, algricultural, \
                    chemical, \
                    feed, soft, soybean, oil, \
                    construction, coal, \
                    equity, \
                    headers, dtypes, grp_dtypes, \
                    h5_path

import pandas as pd
import numpy as np
import colorama
from logErr import logger

colorama.init(autoreset=True)

print headers
full_headers = headers
headers.remove('Date_time')
print headers

def combineSymbolGrp(group_name):
    symbol_array = symbol_d[group_name]
    print "current group: ", group_name
    print "symbol array: ", symbol_array
#    df = pd.DataFrame(columns=full_headers)  # construct a dataframe for combination symbol table
#    df = df.astype(dtype=dtypes)
    # if not dfo is None:
    df_l = []
    try:
        with pd.HDFStore(h5_path) as f:
            for symbol in symbol_array:
                print "parsing symbol: " + symbol
                df_a = pd.read_hdf(f, '/' + symbol, mode='r', columns=headers)
                print "df_a data types: ", df_a.dtypes
                print "df_a: ", df_a.index, '\n', df_a
                df_l.append(df_a)
    #                    df = pd.concat([df, df_a], axis=0).groupby('Date_time').sum().reset_index()
    #            df = df.radd(df_a, fill_value=0)
            df = reduce(lambda x, y: x.add(y, fill_value=0), df_l)
            print "df:   ", '\n', df.index, df
            df = df / len(symbol_array)
            dfo = pd.DataFrame(columns=headers)
            dfo.astype(dtype=grp_dtypes)
            dfo = pd.read_hdf(f, '/'+group_name, mode='r', columns=headers)

    except KeyError:
        print colorama.Fore.BLUE + "Symbol not found in H5, create an empty Dataframe."
        pass
    except Exception as e:
        print colorama.Fore.RED + "Table not exist or Error reading H5."
        logger.error('Failed to read excel or h5: ' + str(e))

    if df.equals(dfo):
        print "Data not changed! break."
    else:
        try:
            with pd.HDFStore(h5_path) as f:
                df_date = pd.read_hdf(f, '/Date', mode='r')
                print "df_date: ", '\n', df_date
#                df = pd.concat([df_date, df], axis=1)
#                df.insert(0, 'Date_time', df_date['Date_time'], allow_duplicates=False)
                df = pd.merge(df_date, df, how='inner', left_index=True, right_index=True)
                print "df:   ", '\n', df.index, df
                df.to_hdf(f, '/'+group_name, format='table', append=False, data_columns=True, mode='a')
        except Exception as e:
            logger.error('Failed to read excel or h5: ' + str(e))
            print str(e)

def createSymbolGrp(symbol_array):
    df_date = pd.DataFrame(columns='Date_time', dtypes='datetime64[ns]')
    i = 0
    for symbol in symbol_array:
        i += 1
        print "parsing symbol: " + symbol
        df_a = pd.read_hdf(f, '/' + symbol, mode='r')
        print "df_a data types: ", df.dtypes
        print "df_a: ", df_a.index, '\n', df_a
        df = pd.concat([df, df_a], axis=0).groupby('Date_time').sum().reset_index()
    #            df = df.radd(df_a, fill_value=0)
    print "df:   ", '\n', df.index, df
    df = df / i

    return

def updateSymbolGrp(symbol_array):
    return

for symbol_key in symbol_d:
    combineSymbolGrp(symbol_key)



