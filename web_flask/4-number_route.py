#!/usr/bin/python3
''' Flask application '''
from flask import Flask, escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    ''' root endpoint for flask app'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' path hbnb which returns a string'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def fun(text):
    ''' path c which returns says c is fun'''
    return 'C %s' % escape(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def p_fun(text):
    ''' path c which returns says c is fun'''
    return 'Python %s' % escape(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def n_umber(n):
    ''' path n accepts an integer'''
    return '%d is a number' % n


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)