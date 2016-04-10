import pymongo
import settings


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,
                                        cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ClassProperty(property):
    def __get__(self, cls, owner):
        return self.fget.__get__(None, owner)()


class MongoDB(object):

    """
    MongoDB implemented like a singleton
    """
    __metaclass__ = Singleton
    _db = None

    @ClassProperty
    @classmethod
    def db(cls):
        if not cls._db:
            tmp = pymongo.MongoClient(host=settings.MONGODB['HOSTS'])
            cls._db = tmp[settings.MONGODB['DBNAME']]
        return cls._db

    @classmethod
    def get(cls):
        return cls.db
