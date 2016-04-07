from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
from modules.database import MongoDB
from re import sub


class M_news(object):

    @classmethod
    def tags(cls, tags, page):
        result = list(MongoDB.get().posts.find(
            {'tags': {'$in': tags}}).sort("_id", -1).skip(page * 10).limit(10))
        result2 = MongoDB.get().posts.find({'tags': {'$in': tags}}).count()

        return {'result': result, 'n_posts': result2, 'page': page}

    @classmethod
    def news(cls, page):
        result = list(
            MongoDB.get().posts.find().sort("_id", -1).skip(page * 10).limit(10))

        return {'result': result,
                'n_posts': MongoDB.get().posts.count(),
                'page': page}

    @classmethod
    def new_comment(cls, id_post, texto, ip, auth_user):
        user = MongoDB.get().users.find_one({'id': auth_user['id']})
        append_dict = {'user': user,
                       'texto': sub('<[^<]+?>', '', texto),
                       'ip': ip,
                       'date': datetime.now()}
        MongoDB.get().posts.update({'_id': ObjectId(id_post)},
                                   {'$push': {'comments': append_dict}})

    @classmethod
    def new_detailed(cls, _id):
        return MongoDB.get().posts.find_one({'_id': ObjectId(_id)})
