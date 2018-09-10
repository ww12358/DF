# -*- coding:utf-8 -*-

import pandas as pd
import sys
import colorama
from include import excel_path, h5_path, headers, dtypes
from logErr import logger


colorama.init(autoreset=True)
#check date/time
#

def updateDatetime(dateTbl, df):
    dfo = pd.DataFrame(columns=['Date_time'])  # construct a dataframe
    dfo = dfo.astype(dtype={'Date_time': 'datetime64[ns]'})
    with pd.HDFStore(h5_path) as f:
        try:
            dfo = pd.read_hdf(f, '/'+dateTbl, mode='a')
    #            print "dfo: ", dfo.dtypes, '\n', dfo
        except KeyError:  # there is no table called 'symbol' in H5, use an empty dataframe for dfo
            print colorama.Fore.BLUE + "Date_time table not found in H5, create an empty Dataframe."
        except ValueError:
            print colorama.Fore.BLUE + "Symbol not found in H5, create an empty Dataframe."
        except Exception as e:
            print colorama.Fore.RED + "Error reading excel file, exit."
            logger.error('Failed to read h5: %s'  % str(e))
            print str(e)
            sys.exit(1)  # exit with integer 1 if error reading excel file

        if not dfo.equals(df):
            print "date_time: ", df.dtypes, '\n', df
            df.to_hdf(f, '/'+dateTbl, format='table', append=False, data_columns=True, mode='a')
        else:
            print "Date_time need not to be updated. Skip."
            logger.info('Date_time already is updated!')

        f.flush()
        f.close()

    return

def copyDataFromExl(symbol, df, f):
# read h5 to dfo
    try:
        dfo = pd.DataFrame(columns=headers)         #construct a dataframe
        dfo = dfo.astype(dtype=dtypes)
        print colorama.Fore.BLUE + "Reading H5..."

        with pd.HDFStore(h5_path) as f:
            dfo = pd.read_hdf(f, '/'+symbol, mode='a')
#            print "dfo data types: ", dfo.dtypes
            if dfo is None:
                print colorama.Fore.BLUE + "Symbol found in H5, but talbe empty, create an empty Dataframe."

    except KeyError:  # there is no table called 'symbol' in H5, use an empty dataframe for dfo
        #    if dfo is None:
        print colorama.Fore.BLUE + "Symbol not found in H5, create an empty Dataframe."
        pass

#    except FileNotFoundError as fnf_error:
#        print colorama.Fore.RED + "Error reading H5. Exit!", fnf_error
#        exit(2)
    except:
        print colorama.Fore.RED + "Table not exist or Error reading H5."
    #    sys.exit(2)     #exit with integer 2 if error reading hdf5 file

    # compare H5 and excel dataframe, find list of new data to be append and store in df_new, update the rest if need
    i1 = df.set_index('Date_time').index
    if not dfo is None:
        i2 = dfo.set_index('Date_time').index
    else:
        i2 = []
    df_new = df[~i1.isin(i2)]
    df_edit = df[i1.isin(i2)]

    if df_new.empty:  # no data to be appended
        if df.equals(dfo):  # dataframe is not edited
            print "Table not changed! Skip..."
        else:  # dataframe is edited, just update df
            print "Dataframe is edited, update data!"
            df.to_hdf(f, '/'+symbol, format='table', append=False, data_columns=True, mode='a')
    else:
        if df_edit.equals(dfo):  # rows to be appended but previous data was not edited
            #        print "same dataframe, no data need to be edited"
            print "Dataframe was not edited. Rows to be appended..."
            df_new.to_hdf(f, '/'+symbol, format='table', append=True, data_columns=True, mode='a')

        else:  # rows to be appended and previouse dataframe to be updated
            print "Dataframe was edited, New data rows found. \n Update the entire talbe with merged dataframe."
            dfo.update(df_edit)
            dfc = dfo.append(df_new)
            dfc = dfc.astype(dtype=dtypes)
            #print 'dfc', '\n', dfc, '\n', dfc.dtypes
            #        print dfc.index
            #        dfc.set_index('Date_time')
            #        dfc.reset_index(inplace=True, drop = True)      #remove redundency
            #        print colorama.Fore.BLUE+'Index for dfc to save', '\n', dfc.index
            dfc.to_hdf(f, '/'+symbol, format='table', append=False, data_columns=True, mode='a')  # update the entire talbe with combined dataframe dfc

def copySglDataFromExl(symbol):
    try:
        print colorama.Fore.BLUE + "Parsing Excel file..."
        #    xl = pd.ExcelFile(excel_path)   #'/home/sean/Nutstore/DY强弱记录(2018).xlsm')
        df = pd.read_excel(excel_path, sheet_name=symbol, names=headers, header=None, skiprows=2)
        #        df.reset_index(drop=True)
        if df is None:
            print colorama.Fore.GREEN + "Empty excel, nothing to change, exit..."
            exit(1)  # empty excel or excel file corrupted
        else:
            # dataframe from excel contains different data types, convert data types
            df = df.astype(dtype=dtypes)
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
            dfo = pd.read_hdf(f, '/'+symbol, mode='a')
#            print "dfo data types: ", dfo.dtypes
            if dfo is None:
                print colorama.Fore.BLUE + "Symbol found in H5, but talbe empty, create an empty Dataframe."

    except KeyError:  # there is no table called 'symbol' in H5, use an empty dataframe for dfo
        #    if dfo is None:
        print colorama.Fore.BLUE + "Symbol not found in H5, create an empty Dataframe."
        pass

#    except FileNotFoundError as fnf_error:
#        print colorama.Fore.RED + "Error reading H5. Exit!", fnf_error
#        exit(2)
    except:
        print colorama.Fore.RED + "Table not exist or Error reading H5."

    # compare H5 and excel dataframe, find list of new data to be append and store in df_new, update the rest if need
    i1 = df.set_index('Date_time').index
    if not dfo is None:
        i2 = dfo.set_index('Date_time').index
    else:
        i2 = []

    df_new = df[~i1.isin(i2)]
    df_edit = df[i1.isin(i2)]

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
                dfc.to_hdf(f, '/'+symbol, format='table', append=False, data_columns=True,
                           mode='a')  # update the entire talbe with combined dataframe dfc
                print "update the entire talbe with combined dataframe dfc"
                f.flush()
                f.close()