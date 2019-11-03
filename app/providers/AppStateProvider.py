"""A AppStateProvider Service Provider."""
from masonite import request
from masonite.provider import ServiceProvider
from masonite.request import Request
from masonite.view import View

from app.State import AppState


class AppStateProvider(ServiceProvider):
    """Provides App State To The Service Container."""

    wsgi = True

    def register(self):
        pass

    def boot(self, request: Request, view: View):
        state = AppState()
        view.share({"state": state.get(request)})
