from google.cloud import ndb
from shared.system.base.model import BaseModel
from shared.model.garage import Garage

class Car(BaseModel):
    """The Car model"""
    garage = ndb.KeyProperty(kind=Garage)
    plate = ndb.StringProperty()
    brand = ndb.StringProperty()

    @classmethod
    def list(cls, garage=None, plate=None, brand=None, limit=20):
        with cls.ndb_context():
            query = Car.query()
            if garage:
                query = query.filter(Car.garage == garage)
            if plate:
                query = query.filter(Car.plate == plate)
            elif brand:
                query = query.filter(Car.brand == brand)
            if limit:
                return query.fetch(limit)

            return query.fetch()
        
    @classmethod
    def create(cls, garage, plate, brand):
        with cls.ndb_context():
            if not garage:
                raise ValueError("Garage with key {} does not exist".format(garage))
            car = cls(
                garage=garage.key,
                plate=plate,
                brand=brand
            )
            car.put()
            return car