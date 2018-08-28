
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal
import sys
import colorama
from include import symbol_collection, excel_path, h5_path, headers, dtypes
from logErr import logger


colorama.init(autoreset=True)
#check date/time
#

def updateDatetime(dateTbl):
    dfo = pd.DataFrame(columns=['Date_time'])  # construct a dataframe
    dfo = dfo.astype(dtype={'Date_time': 'datetime64[ns]'})
    df = pd.DataFrame(columns=['Date_time'])  # construct a dataframe
    df = dfo.astype(dtype={'Date_time': 'datetime64[ns]'})
    try:
        df = pd.read_excel(excel_path, sheet_name=dateTbl, names=['Date_time'], header=None, skiprows=2)      #read excel
#        df.reset_index(drop=True, inplace=True)
#        df.drop(df.index[0], inplace=True)
#        df = df.astype(dtype={'Date_time':'datetime64[ns]'})

#        dfo = pd.DataFrame(columns=headers)
        with pd.HDFStore(h5_path) as f:
            dfo = pd.read_hdf(f, '/'+dateTbl, mode='r')
#            if dfo is None:
            print "dfo: ", dfo.dtypes, '\n', dfo

    except KeyError:  # there is no table called 'symbol' in H5, use an empty dataframe for dfo
        #    if dfo is None:
        print colorama.Fore.BLUE + "Date_time table not found in H5, create an empty Dataframe."

    except ValueError:
        print colorama.Fore.BLUE + "Symbol not found in H5, create an empty Dataframe."
        pass

    except Exception as e:
        print colorama.Fore.RED + "Error reading excel file, exit."
        logger.error('Failed to read excel or h5: ' + str(e))
        print str(e)
        sys.exit(1)  # exit with integer 1 if error reading excel file

    if not dfo.equals(df):
        with pd.HDFStore(h5_path) as f:
            print "date_time: ", df.dtypes, '\n', df
            df.to_hdf(f, '/'+dateTbl, format='table', append=False, data_columns=True, mode='a')
    else:
        logger.info('Date_time already is updated!')

    return
# read excel file to df
#
def copyDataFromExl(symbol):
    try:
        print colorama.Fore.BLUE + "Parsing Excel file..., Symbol:   ", symbol
        #    xl = pd.ExcelFile(excel_path)   #'/home/sean/Nutstore/DY强弱记录(2018).xlsm')
        df = pd.read_excel(excel_path, sheet_name=symbol, names=headers, header=None, skiprows=2)
        df.reset_index(drop=True)
        if df is None:
            print colorama.Fore.GREEN + "Empty excel, nothing to change, exit..."
            exit(1)  # empty excel or excel file corrupted
        else:
#            df.drop(df.index[0], inplace=True)  # drop blank line
            df = df.astype(dtype=dtypes)  # dataframe from excel contains different data types, convert data types


    except:
        print colorama.Fore.RED + "Error reading excel file, exit."
        sys.exit(1)  # exit with integer 1 if error reading excel file

# read h5 to dfo
#
    try:
        dfo = pd.DataFrame(columns=headers)         #construct a dataframe
        dfo = dfo.astype(dtype=dtypes)
        print colorama.Fore.BLUE + "Reading H5..."

        with pd.HDFStore(h5_path) as f:
            dfo = pd.read_hdf(f, '/' + symbol, mode='a')
#            print "dfo data types: ", dfo.dtypes
            if dfo is None:
                print colorama.Fore.BLUE + "Symbol found in H5, but talbe empty, create an empty Dataframe."
#                dfo = pd.DataFrame(columns=headers)
#                dfo = dfo.astype(dtype=dtypes)
                #        dfo.set_index('Date_time', inplace=True, drop=False)
    #        f.close()
    except KeyError:  # there is no table called 'symbol' in H5, use an empty dataframe for dfo
        #    if dfo is None:
        print colorama.Fore.BLUE + "Symbol not found in H5, create an empty Dataframe."
        pass

#    except FileNotFoundError as fnf_error:
#        print colorama.Fore.RED + "Error reading H5. Exit!", fnf_error
#        exit(2)
    except:
        print colorama.Fore.RED + "Table not exist or Error reading H5."


    #    print 'Error reading H5 '
    #    sys.exit(2)     #exit with integer 2 if error reading hdf5 file


    # diff_pd(df, dfo)
    # print 'df', '\n\n\n', df
    # print '\x1b[6;30;42m', 'dfo', '\n', dfo, '\x1b[0m'

    # print colorama.Fore.BLUE +"data type after converting dataframe from excel file", '\n' , df.dtypes
    # dfo.drop(dfo.index[0], inplace=True)
    # df = df[['Date_time', 'st_pct', 'sw_pct', 'tr_pct', 'tt_pct']]

    # dfa = df.iloc[df['Date_time'] == dfo['Date_time']]
    # df.set_index('Date_time', inplace=True, drop=False)
    # dfo.set_index('Date_time', inplace=True, drop=False)

    # compare H5 and excel dataframe, find list of new data to be append and store in df_new, update the rest if need
    i1 = df.set_index('Date_time').index
    if not dfo is None:
        i2 = dfo.set_index('Date_time').index
    else:
        i2 = []

    df_new = df[~i1.isin(i2)]
#    df_new = df.astype(dtype=dtypes)
    df_edit = df[i1.isin(i2)]
#    df_edit = df.astype(dtype=dtypes)
    # print df.index
    # print '\x1b[6;30;42m', dfo.index, '\x1b[0m'
    # print i1
    # print '\x1b[6;30;42m', i2, '\x1b[0m'
    # print ~i1.isin(i2)

#    print 'df_new', '\n', df_new, df_new.dtypes


    # df_edit = df_edit.astype(dtype=dtypes)
    # df_edit.set_index('Date_time', inplace=True, drop=False)
#    print 'df_edit', '\n', df_edit, df_edit.dtypes

    # print df_edit.equals(dfo),  "same dataframe, no data need to be edited"
    # print df_edit.dtypes

    # assert_frame_equal(df[i1.isin(i2)], dfo, check_like=True)

    if df_new.empty:  # no data to be appended
        print "no data to append, (df_new is empty)"
        if df.equals(dfo):  # dataframe is not edited
            print "nothing changed!"
        else:  # dataframe is edited, just update df
            print "dataframe is edited, just update dfo with df"
            # dfo.update(df)
            with pd.HDFStore(h5_path) as f:
                df.to_hdf(f, '/'+symbol, format='table', append=False, data_columns=True, mode='a')
                f.flush()
                f.close()
    else:
        if df_edit.equals(dfo):  # rows to be appended but previous data was not edited
            #        print "same dataframe, no data need to be edited"
            with pd.HDFStore(h5_path) as f:
                df_new.to_hdf(f, '/'+symbol, format='table', append=True, data_columns=True, mode='a')
                print "rows to be appended but previous data was not edited"
                f.flush()
                f.close()

        else:  # rows to be appended and previouse dataframe to be updated
            dfo.update(df_edit)
            dfc = dfo.append(df_new)
            dfc = dfc.astype(dtype=dtypes)
            #print 'dfc', '\n', dfc, '\n', dfc.dtypes
            #        print dfc.index
            #        dfc.set_index('Date_time')
            #        dfc.reset_index(inplace=True, drop = True)      #remove redundency
            #        print colorama.Fore.BLUE+'Index for dfc to save', '\n', dfc.index
            with pd.HDFStore(h5_path) as f:
                dfc.to_hdf(f, '/' + symbol, format='table', append=False, data_columns=True,
                           mode='a')  # update the entire talbe with combined dataframe dfc
                print "update the entire talbe with combined dataframe dfc"
                f.flush()
                f.close()

updateDatetime('Date')
for symbol in symbol_collection:
    copyDataFromExl(symbol)
