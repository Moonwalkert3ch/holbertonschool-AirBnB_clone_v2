#!/usr/bin/python3
"""Start web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """Return string
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return string
    """
    return 'HBNB'


@app.route('/c/<text>')
def fun_with_c(text):
    """Return text
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """Reformat text
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n=None):
    """Allow request if valid integer
    """
    return str(n) + ' is a number'


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
