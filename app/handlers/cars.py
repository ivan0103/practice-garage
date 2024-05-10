from flask import Blueprint, abort, jsonify, request
from google.cloud import ndb  # Import ndb from google.cloud
from shared.model.garage import Garage
from shared.model.car import Car  # Import the Car model
import logging
import json

bp = Blueprint(name='garage_cars', import_name=__name__, url_prefix='/garages/<garage_id>/cars')

@bp.route('/', methods=["GET"])
def get_garage_cars(garage_id):
    print("GET")
    # for g in Car.list():
    #     g.delete()
    #     print(g)
    cars = Car.list(garage_id = garage_id)
    # Convert cars to a list of dictionaries for JSON serialization
    car_list = [
        {
            'id': car.id,
            'garage_id': garage_id,
            'plate': car.plate,
            'brand': car.brand
        }
        for car in cars
    ]
    return jsonify(car_list)


@bp.route('/', methods=["POST"])
def car_add(garage_id):  # Change parameter name from garage to garage_id
    print("POST")
    # for g in Car.list():
    #     g.delete()
    #     print(g)
    data = request.json
    garage = Garage.get(key=garage_id)
    if (garage is None):
        return jsonify({'error': 'Garage not found'}), 404
    car = Car.add(
        props={
            'garage_id': int(garage_id),
            'plate': data['plate'],
            'brand': data['brand']
        }
    )
    print(car)
    return jsonify({
        'car': {
            'id': car.id,
            'garage_id': garage_id,
            'plate': car.plate,
            'brand': car.brand
        }
    })