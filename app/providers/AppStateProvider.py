"""A ViewComposerProvider Service Provider."""
import json

from masonite.provider import ServiceProvider
from masonite.request import Request
from masonite.view import View


class ViewComposerProvider(ServiceProvider):
    """Provides App State To The Service Container."""

    wsgi = False

    def register(self):
        pass

    def boot(self, view: View, request: Request):
        state = self.get_app_state(request)
        view.share({"state": state})

    def get_app_state(self, request):
        state = {"user": {"loggedIn": True if request.user else False}}
        return state
