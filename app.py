# -*- coding:utf-8 -*-
from flask import Flask, render_template, request
from flask import render_template
from bokeh.plotting import figure
from bokeh.embed import components
import pandas as pd
from bokeh.models import DatetimeTickFormatter
from datetime import datetime as dt

symbol_collection=['A','M','Y', 'P', 'C','JD',
                   'SR', 'CF', 'WH', 'OI', 'RM',  'RS', 'RI',
                   'CU', 'AL', 'ZN', 'PB', 'RU', 'AU', 'AG', 'RB',
                   'TA', 'ME', 'ZC', 'FG',
                   'PP', 'L', 'V', 'I', 'J', 'JM'
                   'IF', 'IH', 'IC', 'TF'
                   ]

app = Flask(__name__)
@app.route('/dashboard/')
def show_dashboard():
    plots = []
    plots.append(make_plot())

    return render_template('dashboard.html', plots=plots)

def make_plot(symbol):
    print 'ploting symbol %s' % symbol
    xl = pd.ExcelFile('data/data.xlsm')
    try:
         df = xl.parse(symbol)

    except:

        print 'Error opening excel file'

    df.drop(df.index[0], inplace=True)
    df = df[['Date_time', 'st_pct', 'sw_pct', 'tr_pct', 'tt_pct']]
    plot = figure(plot_height=250, x_axis_type='datetime', sizing_mode='scale_width')

    x = pd.to_datetime(df['Date_time'])
    y = df['sw_pct']

    plot.line(x, y, line_width=4)
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

@app.route('/handle_data', methods=['POST'])
def handle_data():
    str = request.form['symbol']
    print str
    return str

@app.route('/<symbol>')
def show_detail(symbol):
    symbol = symbol.upper()
    current_symbol = request.args.get("current_symbol")
    if current_symbol == None:
        symbol = "A"
    else:
        symbol = current_symbol.upper()
    if symbol in symbol_collection:
        plots = []
        plots.append(make_plot(symbol))
 #       print 'symbol after uppercase %s' % symbol
        return render_template('dashboard.html', plots=plots)
#    return 'The symbol you required is %s' % symbol

    else:
        return 'The symbol %s you required is not available. Please check' % symbol

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=True,  use_debugger=False, use_reloader=False)