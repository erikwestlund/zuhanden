"""The HomeController Module."""
from masonite.request import Request

from app.inertia.InertiaResponse import InertiaResponse


class IndexController:
    def show(self, inertia: InertiaResponse, request: Request):
        return inertia.render("Index")
