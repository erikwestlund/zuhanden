import json

from app.UserOptions import UserOptions


class UserObserver(object):
    def created(self, user):
        UserOptions.create({
            "user_id": user.id,
            "options": json.dumps({
                "show_email": False
            })
        })
