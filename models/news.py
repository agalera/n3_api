from bson.objectid import ObjectId
from datetime import datetime
from modules.database import MongoDB
from re import sub


class M_news(object):

    @classmethod
    def tags(cls, tags, page):
        result = list(MongoDB.db.posts.find(
            {'tags': {'$in': tags}},
            {'date': True,
             'texto': True,
             'title': True,
             'comments': True,
             'tags': True}).sort("_id", -1).skip(page * 10).limit(10))
        result2 = MongoDB.db.posts.find({'tags': {'$in': tags}}).count()

        return {'result': result, 'n_posts': result2, 'page': page}

    @classmethod
    def news(cls, page):
        # TODO
        result = list(
            MongoDB.db.posts.find(
                {}, {'date': True,
                     'texto': True,
                     'title': True,
                     'comments': True,
                     'tags': True}).sort("_id",
                                         -1).skip(page * 10).limit(10))

        return {'result': result,
                'n_posts': MongoDB.db.posts.count(),
                'page': page}

    @classmethod
    def new_comment(cls, id_post, texto, ip, auth_user):
        user = MongoDB.db.users.find_one({'id': auth_user['id']})
        append_dict = {'user': user,
                       'texto': sub('<[^<]+?>', '', texto),
                       'ip': ip,
                       'date': datetime.now()}
        MongoDB.db.posts.update({'_id': ObjectId(id_post)},
                                {'$push': {'comments': append_dict}})

    @classmethod
    def new_detailed(cls, _id):
        return MongoDB.db.posts.find_one({'_id': ObjectId(_id)})
