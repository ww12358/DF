# -*- coding:utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/handle_data', methods=['GET', 'POST'])

def handle_data():
    if request.method == 'POST':
        str = request.form['symbol']
        return str

    if request.method == 'GET':
        return('<form id="tfnewsearch" method="post" action="/handle_data" > \
		            <input type="text" class="tftextinput" name="symbol" size="21" maxlength="120"><input type="submit" value="search" class="tfbutton"> \
				    <input type="submit"> \
		        </form>')
    else:
#          return render_template('/static/index.html')
        return "Nothing"

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=True,  use_debugger=True, use_reloader=False)