#!/usr/bin/python3
""" Create a Hello HBNB page that runs on 0.0.0.0:5000"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """the hello_hbnb function"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """just display hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """display c and text without"""
    fin_text = text.replace('_', " ")
    return ('C ' + fin_text)


@app.route('/python')
@app.route('/python/<text>')
def python(text="is cool"):
    """display python and text"""
    fin_text = text.replace('_', " ")
    return ('Python ' + fin_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
