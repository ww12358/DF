# -*- coding:utf-8 -*-
from flask import request

@app.route('/handle_data', methods=['POST'])
def handle_data():
    return request.form['symbol']
    # your code
    # return a response


