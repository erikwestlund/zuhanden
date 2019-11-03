import json


class UserObserver(object):
    def creating(self, user):
        user.options = json.dumps({"show_email": False})
