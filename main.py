from flask import Flask, render_template, request
import pandas as pd
from bkcharts import Histogram
from bokeh.embed import components
from bokeh.io import curdoc
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import PreText, Select
from bokeh.plotting import figure



#app = Flask(__name__)

# Load the Iris Data Set
#wb = openpyxl.load_workbook("data/data.xlsm", data_only=True)
#sht = wb.get_sheet_by_name('A')
xl = pd.ExcelFile('data/data.xlsm')
dfa = xl.parse("A")
dfm = xl.parse("M")
dfy = xl.parse("Y")

dfa = dfa[['Date_time','st_pct', 'sw_pct', 'tr_pct', 'tt_pct']]
dfm = dfm[['Date_time','st_pct', 'sw_pct', 'tr_pct', 'tt_pct']]
dfy = dfy[['Date_time','st_pct', 'sw_pct', 'tr_pct', 'tt_pct']]
dfa.drop(dfa.index[0], inplace = True)
dfm.drop(dfm.index[0], inplace = True)
dfy.drop(dfm.index[0], inplace = True)

#print dfa

#iris_df = pd.read_csv("data/iris.data",
#    names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])
#feature_names = iris_df.columns[0:-1].values.tolist()

# Create the main plot
#def create_figure(current_feature_name, bins):
#	p = Histogram(dfa, current_feature_name, title=current_feature_name, color='Species',
#	 	bins=bins, legend='top_right', width=600, height=400)

	# Set the x axis label
#	p.xaxis.axis_label = current_feature_name

	# Set the y axis label
#	p.yaxis.axis_label = 'Count'
#	return p

# Index page
#@app.route('/')
#def index():
	# Determine the selected feature
#	current_feature_name = request.args.get("feature_name")
#	if current_feature_name == None:
#		current_feature_name = "Sepal Length"

	# Create the plot
#	plot = create_figure(current_feature_name, 10)
		
	# Embed plot into HTML via Flask Render
#	script, div = components(plot)
#	return render_template("iris_index1.html", script=script, div=div,
#		feature_names=feature_names,  current_feature_name=current_feature_name)

stats = PreText(text='', width=500)
source = ColumnDataSource(data=dict(date=[], t1=[], t2=[], t1_returns=[], t2_returns=[]))
source_static = ColumnDataSource(data=dict(date=[], t1=[], t2=[], t1_returns=[], t2_returns=[]))
tools = 'pan,wheel_zoom,xbox_select,reset'

ts1 = figure(plot_width=900, plot_height=200, tools=tools, x_axis_type='datetime', active_drag="xbox_select")
ts1.line('date', 't1', source=source_static)
ts1.circle('date', 't1', size=1, source=source, color=None, selection_color="orange")

def update(selected=None):

    source.data = source.from_df(dfa[['st_pct', 'sw_pct', 'tr_pct', 'tt_pct']])
    source_static.data = source.data
# With debug=True, Flask server will auto-reload
# when there are code changes
#if __name__ == '__main__':
#	app.run(host="0.0.0.0", port=5000, debug=True)

series = column(ts1)
layout = column(series)

update()
curdoc().add_root(layout)
curdoc().title = "Stocks"