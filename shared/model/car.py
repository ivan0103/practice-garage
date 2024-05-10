from google.cloud import ndb
from shared.system.base.model import BaseModel


class Car(BaseModel):
    """The Car model"""
    garage_id = ndb.IntegerProperty(required=True)  # Keep garage_id
    plate = ndb.StringProperty()
    brand = ndb.StringProperty()

    @classmethod
    def list(cls, garage_id=None, plate=None, brand=None, limit=20):
        """
        example normal query with filter.
        """
        with cls.ndb_context():
            query = cls.query()
            if garage_id:
                # Convert garage_id to an integer
                garage_id_int = int(garage_id)
                query = query.filter(cls.garage_id == garage_id_int)
            if plate:
                query = query.filter(cls.plate == plate)
            if brand:
                query = query.filter(cls.brand == brand)
            if limit:
                return query.fetch(limit)
            return query.fetch()
        
    @classmethod
    def create(cls, garage_id, plate, brand):
        """Create a new car entity."""
        with cls.ndb_context():
            # Fetch the latest car entity to determine the next ID
            latest_car = cls.query().order(-cls.key).get()
            next_id = 1 if latest_car is None else latest_car.id + 1

            # Create the car entity with the manually assigned ID
            car = cls(
                id=next_id,  # Use id instead of garage_id
                garage_id=garage_id,  # Keep garage_id
                plate=plate,
                brand=brand
            )
            car.put()
            return car
        

# @bp.route('/', methods=["PUT"])
# def garage_update():
#     props = request.json
#     garage = Garage.get(key=props.pop('id'))
#     garage.update(props=props)
#     return jsonify({
#         'garage': {
#             'id': garage.id,
#             'name': garage.name,
#             'brand': garage.brand,
#             'postal_country': garage.postal_country
#         }
#     })

# @bp.route('/', methods=["DELETE"])
# def garage_delete():
#     props = json.loads(request.data)
#     garage_id = props['garage']
#     if garage_id is None:
#         return jsonify({'error': 'Garage ID not provided'}), 400
#     garage = Garage.get(key=garage_id)
#     if garage is None:
#         return jsonify({'error': 'Garage not found'}), 404
#     garage.delete()
#     return jsonify({
#         'garage': {
#             'id': garage.id,
#             'name': garage.name,
#             'brand': garage.brand,
#             'postal_country': garage.postal_country
#         }
#     })