# -*- coding:utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/handle_data', methods=['GET', 'POST'])

def handle_data():
    if request.method == 'POST':
        str = request.form['symbol']
        return str

    if request.method == 'GET':
        return render_template('query.html')

    else:
#          return render_template('/static/index.html')
        return "Oops! Something went wrong..."

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=True,  use_debugger=True, use_reloader=False)