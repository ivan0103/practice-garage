# flake8: noqa
import os
_credentials = None
_project = None
debug = os.environ.get('FLASK_ENV', 'prod') == 'development'

from flask import Flask, render_template, jsonify, request

from shared.system import datastore
from shared.model.garage import Garage
from shared.model.car import Car
from google.cloud import ndb
from handlers import garages
from handlers import cars

app = Flask(__name__)
app.register_blueprint(garages.bp)
app.register_blueprint(cars.bp)



@app.route('/health-check')
def root():
    return 'Ok'

@app.route('/')
def testing():
    return render_template('index.html')

@app.route('/test-create')
def test_create():
    with datastore.client.context():
        g = Garage(name='vigo', brand='opel', postal_country='NL')
        g.put()
        garages = [g for g in Garage.query()]
        return jsonify([{'name': g.name} for g in garages])

@app.route('/test')
def test_list():
    with datastore.client.context():
        garages = [g for g in Garage.query()]
        return jsonify([{'name': g.name} for g in garages])

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
