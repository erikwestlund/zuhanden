"""The HomeController Module."""

from app.inertia.InertiaResponse import InertiaResponse


class IndexController:

    def show(self, inertia: InertiaResponse):
        return inertia.render("Index")
