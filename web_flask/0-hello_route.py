#!/usr/bin/python3
""" Create a Hello HBNB page that runs on 0.0.0.0:5000"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    "the hello_hbnb function"
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
