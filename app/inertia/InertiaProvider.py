from masonite.provider import ServiceProvider

from app.inertia.InertiaResponse import InertiaResponse


class InertiaProvider(ServiceProvider):
    """Registers classes for InertiaJS responses."""

    wsgi = False

    def register(self):
        self.app.bind("Inertia", InertiaResponse(self.app))
