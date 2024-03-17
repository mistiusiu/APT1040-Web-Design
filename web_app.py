#!/usr/bin/python3
""" Starts a Flask Web Application """
from models import storage
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/', strict_slashes=False)
def hbnb():
    """ The Web App is alive! """
    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.title)

    return render_template('index.html',
                           places=places, cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)