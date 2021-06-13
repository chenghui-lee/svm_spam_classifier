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
    print(text, p)
    return 'spam' if p else 'not spam'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
