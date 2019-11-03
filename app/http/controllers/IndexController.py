"""The HomeController Module."""

from masonite.auth import Auth
from masonite.request import Request
from masonite.view import View

from app.State import AppState


class IndexController:
    """Home Dashboard Controller."""

    def __init__(self):
        pass

    def show(self, request: Request, view: View):
        state = AppState()
        return view.render("index")
