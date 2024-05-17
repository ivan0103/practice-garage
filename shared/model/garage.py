from google.cloud import ndb
from shared.system.base.model import BaseModel


class Garage(BaseModel):
    """The Garage model"""

    name = ndb.StringProperty(required=True)
    brand = ndb.StringProperty()

    postal_country = ndb.StringProperty()

    note = ndb.TextProperty(indexed=False)

    @classmethod
    def list(cls, name=None, brand=None, limit=20):
        """
        example normal query with filter.

        """
        with cls.ndb_context():
            query = Garage.query()
            if name:
                query = query.filter(Garage.name == name)
            if brand:
                query = query.filter(Garage.brand == brand)
            if limit:
                return query.fetch(limit)
            return query.fetch()