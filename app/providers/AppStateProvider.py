"""A ViewComposerProvider Service Provider."""
import json

from masonite.provider import ServiceProvider
from masonite.request import Request
from masonite.view import View


class AppStateProvider(ServiceProvider):
    """Provides App State To The Service Container."""

    def register(self):
        pass

    def boot(self, view: View, request: Request):
        state = self.get_app_state(request)
        view.share({"state": state})

    def get_app_state(self, request):
        user = request.user()
        state = {
            "user": {
                "name": user.name if user else None,
                "loggedIn": True if user else False,
            }
        }

        return json.dumps(state) if state else {}
