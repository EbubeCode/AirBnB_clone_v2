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


@app.route('/states', strict_slashes=False)
def states():
    '''gets the list of states'''
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    return render_template('9-states.html', states=states)

@app.route('/states/<id>', strict_slashes=False)
def state(id):
    '''gets the list of states'''
    key = f'State.{id}'
    state = storage.all(State).get(key)
    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
