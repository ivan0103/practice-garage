from flask import Blueprint, abort, jsonify, request
from google.cloud import ndb
from shared.model.garage import Garage
from shared.model.car import Car
import logging
import json

bp = Blueprint(name='garage_cars', import_name=__name__, url_prefix='/garages/<garage_id>/cars')

@bp.route('/', methods=["GET"])
def get_garage_cars(garage_id):
    garage = Garage.get(garage_id)
    if garage is None:
        return jsonify({'error': 'Garage not found'}), 404
    cars = Car.list(garage=garage.key)
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
def car_add(garage_id):
    data = request.json
    garage = Garage.get(key = garage_id)
    if garage is None:
        return jsonify({'error': 'Garage not found'}), 404
    car = Car.create(
        garage,
        plate=data['plate'],
        brand=data['brand']
    )
    return jsonify({
        'id': car.id,
        'garage_id': garage_id,
        'plate': car.plate,
        'brand': car.brand
    })

@bp.route('/<car_id>', methods=["PUT"])
def car_update(garage_id, car_id):
    props = request.json
    print(props)
    car = Car.get(key=car_id)
    car.update(props=props)
    return jsonify({
            'id': car.id,
            'garage_id': garage_id,
            'plate': car.plate,
            'brand': car.brand
    })

@bp.route('/<car_id>', methods=["DELETE"])
def car_delete(garage_id, car_id):
    print("DELETE")
    if garage_id is None:
        return jsonify({'error': 'Garage ID not provided'}), 400
    garage = Garage.get(key=garage_id)
    if garage is None:
        return jsonify({'error': 'Garage not found'}), 404
    if car_id is None:
        return jsonify({'error': 'Car ID not provided'}), 400
    car = Car.get(key=car_id)
    if car is None:
        return jsonify({'error': 'Car not found'}), 404
    
    car.delete()
    return jsonify({
            'id': car.id,
            'garage_id': garage_id,
            'plate': car.plate,
            'brand': car.brand
    })