import pymongo
import threading
import settings

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MongoDB(object):

    """
    MongoDB implemented like a singleton
    """
    __metaclass__ = Singleton
    _db = pymongo.MongoClient(host=settings.MONGODB['HOSTS'],
                              connect=False)[settings.MONGODB['DBNAME']]

    @classmethod
    def get(cls):
        return cls._db
