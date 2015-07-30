import pymongo
import threading
import settings


class MongoDB(object):

    """
    MongoDB implemented like a singleton
    """
    __singleton_lock = threading.Lock()
    _db = None

    @classmethod
    def get(cls):
        if not cls._db:
            try:
                cls.__singleton_lock.acquire()
                # prevent reassign
                if not cls._db:
                    db = pymongo.MongoClient(host=settings.MONGODB['HOSTS'])
                    cls._db = db[settings.MONGODB['DBNAME']]
            finally:
                cls.__singleton_lock.release()
        return cls._db
