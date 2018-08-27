# -*- coding:utf-8 -*-
from flask import Flask, render_template, request
from flask import render_template
from bokeh.plotting import figure
from bokeh.embed import components
import pandas as pd
from bokeh.models import DatetimeTickFormatter
from datetime import datetime as dt
import updateCreekIDX as upd
import sys
from include import *

app = Flask(__name__)
@app.route('/dashboard/')
def show_dashboard():
    plots = []
    plots.append(make_plot())

    return render_template('dashboard.html', plots=plots)

def make_plot(df):
    print df
#    xl = pd.ExcelFile('data/data.xlsm')


#    print df
#    df.drop(df.index[0], inplace=True)
#    df = df[['Date_time', 'st_pct', 'sw_pct', 'tr_pct', 'tt_pct']]
    plot = figure(plot_height=250, x_axis_type='datetime', sizing_mode='scale_width')

 #   x = pd.to_datetime(df['Date_time'])
    x = df['Date_time']
    y = df['sw_pct']
    print y

    plot.line(x, y, line_width=2)
    plot.xaxis.formatter = DatetimeTickFormatter(
        hours=["%Y-%m-%d %H:%M:%S"],
        days=["%Y-%m-%d %H:%M:%S"],
        months=["%Y-%m-%d %H:%M:%S"],
        years=["%Y-%m-%d %H:%M:%S"],
    )

    script, div = components(plot)
    return script, div

@app.route('/hello')
def index():
    return 'Hello, visitor!'

@app.route('/handle_data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        print "POST now!"
        current_symbol = request.form['symbol']
        print current_symbol
        df = parse_symbol(current_symbol)
        plots = []
        plots.append(make_plot(df))
        #       print 'symbol after uppercase %s' % symbol
        return render_template('dashboard.html', plots=plots)
    #    return 'The symbol you required is %s' % symbol

    elif request.method == 'GET':
        return render_template('query.html')

    else:
    # return render_template('/static/index.html')
        return "Oops! Something went wrong..."


#@app.route('/<symbol>')
def show_detail(symbol):
    current_symbol = request.args.get("current_symbol")
    symbol = current_symbol.upper()
    df = parse_symbol(symbol)
    plots = []
    plots.append(make_plot(df))
 #       print 'symbol after uppercase %s' % symbol
    return render_template('dashboard.html', plots=plots)
#    return 'The symbol you required is %s' % symbol

def parse_symbol(symbol):
    df = pd.DataFrame(columns=upd.headers)
    symbol = symbol.upper()

    print symbol

    if symbol in c_idx or symbol in symbol_d:
        print "Single symbol!"
        try:
            df = pd.read_hdf('./data/creekIDX.hdf5', '/' + symbol, mode='r')
        except:
            print 'Data File Error...'
        return df
    else:
        print "Something is wrong"
        return df



if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=True,  use_debugger=False, use_reloader=False)