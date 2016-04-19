from modules.database import MongoDB


class M_login(object):

    @classmethod
    def check_user(cls, session_json):
        # session_json {u'family_name': 'Galera', 'account_type': 0, u'name':
        # 'Alberto Galera', u'picture':
        # 'https://lh4.googleusercontent.com/-iQJC6wC74qY/AAAAAAAAAAI/AAAAAAAAAEA/23bWRPlgCsU/photo.jpg',
        # u'locale': 'es', u'id': '101838179005792233548', u'link':
        # 'https://plus.google.com/101838179005792233548', u'given_name':
        # 'Alberto', u'email': 'galerajimenez@gmail.com', u'verified_email':
        # 'True'}
        user = M_login.get_user(session_json['_id'])
        if user is None:
            session_json['account_type'] = 0
            MongoDB.db.users.insert_one(session_json)
        return user

    @classmethod
    def get_user(cls, _id):
        return MongoDB.db.users.find_one({'_id': _id})
