from google.cloud import ndb
from shared.system.base.model import BaseModel


class Car(BaseModel):
    """The Car model"""

    garage_id = ndb.KeyProperty(kind='Garage', required=True)
    plate = ndb.StringProperty(required=True)
    brand = ndb.StringProperty()
    car_id = ndb.StringProperty()  # ID field for the car

    @classmethod
    def list(cls, garage_id=None, plate=None, brand=None, limit=20):
        """
        example normal query with filter.
        """
        with cls.ndb_context():
            query = cls.query()
            if garage_id:
                query = query.filter(cls.garage_id == ndb.Key('Garage', garage_id))
            if plate:
                query = query.filter(cls.plate == plate)
            if brand:
                query = query.filter(cls.brand == brand)
            if limit:
                return query.fetch(limit)
            return query.fetch()