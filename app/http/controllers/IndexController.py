"""The HomeController Module."""

from masonite.auth import Auth
from masonite.request import Request
from masonite.view import View


class IndexController:
    """Home Dashboard Controller."""

    def __init__(self):
        pass

    def show(self, request: Request, view: View):
        return view.render("index")
