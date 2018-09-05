# -*- coding:utf-8 -*-
from updateData import updateDatetime, copyDataFromExl
from include import symbol_collection
from include import excel_path, h5_path, headers, dtypes
import pandas as pd
import sys
import colorama
from logErr import logger

# read ALL worksheets into a dictionary of dataframes
try:
    print colorama.Fore.BLUE + "Parsing Excel file..."
    #    xl = pd.ExcelFile(excel_path)   #'/home/sean/Nutstore/DY强弱记录(2018).xlsm')
    dfs = pd.read_excel(excel_path, sheet_name=symbol_collection, names=headers, header=None, skiprows=2, dtype=dtypes)
    df_date = pd.read_excel(excel_path, sheet_name='Date', names=['Date_time'], header=None, skiprows=2, dtype='datetime64[ns]')

    if dfs is None:
        print colorama.Fore.GREEN + "Empty excel, nothing to change, exit..."
        exit(1)  # empty excel or excel file corrupted
    else:
        with pd.HDFStore(h5_path) as f:
            for symbol in symbol_collection:
                print symbol
                copyDataFromExl(symbol, dfs[symbol], f)
            f.flush()
            f.close()

except Exception as e:
    print colorama.Fore.RED + "Error reading excel file, exit."
    logger.error('Failed to read excel or h5: %s' % str(e))
    print str(e)
    sys.exit(1)  # exit with integer 1 if error reading excel file

updateDatetime('Date', df_date)

