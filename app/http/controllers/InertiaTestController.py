from masonite.controllers import Controller

from app.inertia.InertiaResponse import InertiaResponse


class InertiaTestController(Controller):
    def show(self, inertia: InertiaResponse):
        return inertia.render("Index", {"test": "test"})
