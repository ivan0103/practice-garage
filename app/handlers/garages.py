from flask import Blueprint, abort, jsonify, request
from shared.model.garage import Garage
import logging
import json

bp = Blueprint(name='garages', import_name=__name__, url_prefix='/garages')

#@bp.route('/', defaults={'page': 'index'})
@bp.route('/', methods=["GET"])
def garage_list():
    print("GET")
    for g in Garage.list():
        print(g)
    if request.args and 'garage' in request.args:
        garage = Garage.get(key=request.args.get('garage'))
        print("INSIDE")
        print(garage)
        return jsonify({
            'garage': {
                'id': garage.id,
                'name': garage.name,
                'brand': garage.brand,
                'postal_country': garage.postal_country
            }
        })
    return jsonify(
        [
            {
                'garage': {
                    'id': g.id,
                    'name': g.name,
                    'brand': g.brand,
                    'postal_country': g.postal_country
                }

            } for g in Garage.list()
        ]
    )


@bp.route('/', methods=["POST"])
def garage_add():
    print("POST")
    garage = Garage.add(props=request.json)
    for g in Garage.list():
        print(g)
    return jsonify({
        'garage': {
            'id': garage.id,
            'name': garage.name,
            'brand': garage.brand,
            'postal_country': garage.postal_country
        }
    })

@bp.route('/', methods=["PUT"])
def garage_update():
    props = request.json
    garage = Garage.get(key=props.pop('id'))
    # print(garage)
    garage.update(props=props)
    return jsonify({
        'garage': {
            'id': garage.id,
            'name': garage.name,
            'brand': garage.brand,
            'postal_country': garage.postal_country
        }
    })

@bp.route('/', methods=["DELETE"])
def garage_delete():
    print("DELETE ALL -----------")
    for g in Garage.list():
        print(g)
        g.delete()
    print("DELETE-------------")
    props = json.loads(request.data)
    print(props)
    garage_id = props['garage']
    print(garage_id)
    if garage_id is None:
        return jsonify({'error': 'Garage ID not provided'}), 400
    garage = Garage.get(key=garage_id)
    print(garage)
    if garage is None:
        return jsonify({'error': 'Garage not found'}), 404
    
    garage.delete()

    return jsonify({
        'garage': {
            'id': garage.id,
            'name': garage.name,
            'brand': garage.brand,
            'postal_country': garage.postal_country
        }
    })