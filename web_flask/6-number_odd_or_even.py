#!/usr/bin/python3
""" Create a Hello HBNB page that runs on 0.0.0.0:5000"""

from flask import Flask
from markupsafe import escape
from flask import render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """display python and text"""
    fin_text = text.replace('_', " ")
    return ('Python ' + fin_text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display the number"""
    return ('{} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ display a html file """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ display if number is even or odd"""
    return render_template('6-number_odd_or_even.html', n=n)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
