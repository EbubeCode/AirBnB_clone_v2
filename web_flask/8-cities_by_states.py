#!/usr/bin/python3
''' Flask application '''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def tear_down(arg):
    '''tears down storage connection'''
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states():
    '''gets the list of states'''
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    print(states[0].cities)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
