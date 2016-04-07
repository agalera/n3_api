from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
from modules.database import MongoDB


class M_login(object):

    @classmethod
    def check_user(cls, kwargs):
        # kwargs {u'family_name': 'Galera', 'account_type': 0, u'name':
        # 'Alberto Galera', u'picture':
        # 'https://lh4.googleusercontent.com/-iQJC6wC74qY/AAAAAAAAAAI/AAAAAAAAAEA/23bWRPlgCsU/photo.jpg',
        # u'locale': 'es', u'id': '101838179005792233548', u'link':
        # 'https://plus.google.com/101838179005792233548', u'given_name':
        # 'Alberto', u'email': 'galerajimenez@gmail.com', u'verified_email':
        # 'True'}
        if MongoDB.db.users.find_one({'_id': kwargs['_id']}) is None:
            print "new user", kwargs
            MongoDB.db.users.insert(kwargs)

    @classmethod
    def get_user(cls, _id):
        return MongoDB.db.users.find_one({'_id': kwargs['_id']})