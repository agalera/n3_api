from datetime import datetime
from modules.database import MongoDB


class M_admin(object):

    @classmethod
    def new_post(cls, account_id, title, texto, tags, ip):
        user = MongoDB.get().users.find_one({'id': account_id})
        return MongoDB.get().posts.insert({'title': title,
                                           'texto': texto,
                                           'ip': ip,
                                           'user': user,
                                           'comments': [],
                                           'tags': tags,
                                           'date': datetime.now()})
