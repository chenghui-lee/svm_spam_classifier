# Main entry point
from flask import Flask, render_template, request, flash, redirect, url_for
import os
import io
import predict as model

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lksm2ns0ma-sks1ns9sna0-sma9qmsm-ams9nnxba12-1283058720x'


@app.route("/")
def index():
    return render_template('main.html')

@app.route('/', methods=['POST'])
def upload():
    text = request.form['text']
    p = model.predict(text)
    res = 'Urh! The message is a spam.' if p else 'Hooray! The message is not a spam.'
    flash(res)
    return index()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
