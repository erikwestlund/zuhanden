"""The HomeController Module."""

from masonite.request import Request
from masonite.view import View

from app.User import User
from app.auth.authenticators import user_can


class IndexController:
    """Home Dashboard Controller."""

    def __init__(self):
        pass


    def show(self, view: View):
        return view.render("index")
