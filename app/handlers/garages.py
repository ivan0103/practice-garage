from flask import Blueprint, abort, jsonify, request
from shared.model.garage import Garage
from shared.model.car import Car
import logging
import json

bp = Blueprint(name='garages', import_name=__name__, url_prefix='/garages')

#@bp.route('/', defaults={'page': 'index'})
@bp.route('/', methods=["GET"])
def garage_list():
    if request.args and 'garage' in request.args:
        garage = Garage.get(key=request.args.get('garage'))
        return jsonify({
                'id': garage.id,
                'name': garage.name,
                'brand': garage.brand,
                'postal_country': garage.postal_country
        })
    return jsonify(
        [
            {
                    'id': g.id,
                    'name': g.name,
                    'brand': g.brand,
                    'postal_country': g.postal_country
            } for g in Garage.list()
        ]
    )


@bp.route('/', methods=["POST"])
def garage_add():
    garage = Garage.add(props=request.json)
    return jsonify({
            'id': garage.id,
            'name': garage.name,
            'brand': garage.brand,
            'postal_country': garage.postal_country
    })

@bp.route('/', methods=["PUT"])
def garage_update():
    props = request.json
    garage = Garage.get(key=props.pop('id'))
    garage.update(props=props)
    return jsonify({
            'id': garage.id,
            'name': garage.name,
            'brand': garage.brand,
            'postal_country': garage.postal_country
    })

@bp.route('/', methods=["DELETE"])
def garage_delete():
    props = json.loads(request.data)
    garage_id = props['garage']
    if garage_id is None:
        return jsonify({'error': 'Garage ID not provided'}), 400
    garage = Garage.get(key=garage_id)
    if garage is None:
        return jsonify({'error': 'Garage not found'}), 404
    garage.delete()

    cars = Car.list(garage_id = garage_id)
    for c in cars:
        c.delete()

    return jsonify({
            'id': garage.id,
            'name': garage.name,
            'brand': garage.brand,
            'postal_country': garage.postal_country
    })