from google.cloud import ndb
import logging

from shared.system import datastore


class MixinDefaults(object):

    def fill(self, props):
        """
        attempts to write props to the model.

        :param props: dict with props ( from json ) thats needs to be set
        :return:
        """
        unused = list()
        if props is None:
            return unused

        for attr, value in props.items():
            try:
                if hasattr(self, attr):
                    setattr(self, attr, value)
                else:
                    unused.append({attr: value})
            except Exception as e:
                logging.exception(e)
                unused.append({attr: value})
        return unused


class BaseModel(ndb.Model, MixinDefaults):

    @property
    def id(self):
        """
        """
        if self.key:
            return self.key.integer_id()
        logging.error("Model %s instance not stored yet!" % self.__class__.__name__)
        return None

    @classmethod
    def ndb_context(cls):
        return datastore.client.context()

    @classmethod
    def get(cls, key, parent=None):
        """
        """
        entity = None
        if key is None:
            return None
        with datastore.client.context():
            entity = cls.get_by_id(int(key), parent)
        return entity

    @classmethod
    def add(cls, props, **kwargs): 
        entity = cls(**props)
        entity.fill(props=props)
        entity.save()
        return entity

    def update(self, props):
        """
        """
        unused = self.fill(props=props)
        if unused:
            logging.info('Not all props have been processed: %s' % unused)
        return self.save()

    def save(self):
        """
        """
        with self.ndb_context():
            return self.put()

    def delete(self):
        with self.ndb_context():
            return self.key.delete()

    def __repr__(self):
        with datastore.client.context():
            return super(BaseModel, self).__repr__()


class HBKeyProperty(ndb.KeyProperty):
    def _to_base_type(self, value):
        if type(value) == HBKeyWrapper:
            return value._key
        return value

    def _from_base_type(self, value):
        return HBKeyWrapper(value)


class HBKeyWrapper(object):
    def __init__(self, key):
        self._key = key

    def get(self):
        with datastore.client.context():
            return self._key.get()

    def get_async(self, **kwargs):
        '''
        kwargs conform :
        ndb.key.Key.get_async
        :param kwargs:
        :return:
        '''
        with datastore.client.context():
            return self._key.get_async(**kwargs)

    @property
    def key(self):
        return self._key

    def __eq__(self, other):
        return self._key.__eq__(other)

    def __lt__(self, other):
        return self._key.__lt__(other)

    def __le__(self, other):
        return self._key.__le__(other)

    def __gt__(self, other):
        return self._key.__gt__(other)

    def __ge__(self, other):
        return self._key.__ge__(other)


# class HBKeyWrapper(ndb.key.Key):
#     def __init__(self, key):
#         self._key = key
#
#     def __new__(cls, *args, **kwargs):
#         for a in args:
#             print(a)
#         for kwa in kwargs:
#             print(kwa)
#
#     # def get(self, **kwargs):
#     #     entity = None
#     #     with datastore.client.context():
#     #         entity = super(HBKeyWrapper, self).get(**kwargs)
#     #     return entity
#
#     def get_async(self, **kwargs):
#         '''
#         kwargs conform :
#         ndb.key.Key.get_async
#         :param kwargs:
#         :return:
#         '''
#         result = None
#         with datastore.client.context():
#             result = super(HBKeyWrapper, self).get_async(**kwargs)
#         return result
