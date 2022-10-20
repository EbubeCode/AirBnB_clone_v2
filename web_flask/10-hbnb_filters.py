#!/usr/bin/python3
''' Flask application '''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def tear_down(arg):
    '''tears down storage connection'''
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def states():
    '''gets the list of states'''
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    amenities = list(storage.all(Amenity).values())
    amenities.sort(key=lambda x: x.name)
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
