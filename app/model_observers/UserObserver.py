from app import UserOptions


class UserObserver(object):

    def saving(self, user):
        pass

    def saved(self, user):
        user_options = UserOptions.where(user.id)

