# Main entry point
from flask import Flask, render_template, request, flash, redirect, url_for
import os
import model
import io


app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'


@app.route("/")
def index():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
