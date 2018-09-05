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
import colorama
from logErr import logger

colorama.init(autoreset=True)

print headers
full_headers = headers
headers.remove('Date_time')
print headers

def combineSymbolGrp(group_name, f, df_date):
    symbol_array = symbol_d[group_name]
    print "current group: ", group_name
#    print "symbol array: ", symbol_array
    df_l = []
    for symbol in symbol_array:
        print "parsing symbol: " + symbol
        df_a = pd.read_hdf(f, '/' + symbol, mode='r', columns=headers)
#        print "df_a data types: ", df_a.dtypes
#        print "df_a: ", df_a.index, '\n', df_a
        df_l.append(df_a)
    df = reduce(lambda x, y: x.add(y, fill_value=0), df_l)          #add up dataframes in df_l
#        print "df:   ", '\n', df.index, df
    df = df / len(symbol_array)

    dfo = pd.DataFrame(columns=headers)
    dfo.astype(dtype=grp_dtypes)
    try:
        dfo = pd.read_hdf(f, '/'+group_name, mode='r', columns=headers)         #read from h5, get group dataframe
    except KeyError:
        print colorama.Fore.BLUE + "Symbol not found in H5, create an empty Dataframe."
        pass
    except Exception as e:
        print colorama.Fore.RED + "Table not exist or Error reading H5."
        logger.error('Failed to read excel or h5: ' + str(e))

    if df.equals(dfo):
        print "Data not changed! Skip."
    else:
        try:
#            print "df_date: ", '\n', df_date
            df = pd.merge(df_date, df, how='inner', left_index=True, right_index=True)
#            print "df:   ", '\n', df.index, df
            df.to_hdf(f, '/'+group_name, format='table', append=False, data_columns=True, mode='a')
        except Exception as e:
            logger.error('Failed to read excel or h5: ' + str(e))
            print str(e)


with pd.HDFStore(h5_path) as f:
    try:
        df_date = pd.read_hdf(f, '/Date', mode='r')
    except Exception as e:
        logger.error('Failed to read excel or h5: ' + str(e))
        print str(e)

    for symbol_key in symbol_d:
        combineSymbolGrp(symbol_key, f, df_date)
    f.flush()
    f.close()


