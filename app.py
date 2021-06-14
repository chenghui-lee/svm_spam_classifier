# Main entry point
from flask import Flask, render_template, request, flash, redirect, url_for
import os
import io
import predict as model

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'


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
    app.run(host='127.0.0.1', port=8000)
