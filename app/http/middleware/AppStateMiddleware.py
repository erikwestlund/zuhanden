"""AppStateFactory Middleware."""

from masonite.request import Request
from masonite.view import View


class AppStateMiddleware:
    """AppStateFactory Middleware."""

    def __init__(self, request: Request, view: View):
        self.request = request
        self.view = view

    def before(self):
        pass

    def after(self):
        state = self.get_app_state()
        self.view.share({"state": state})

    def get_app_state(self):
        user = self.request.user()
        state = {
            "user": {
                "name": user.name if user else None,
                "loggedIn": True if user else False,
            }
        }
        return state
