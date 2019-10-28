"""A Helper Service Provider."""

import builtins
from masonite.provider import ServiceProvider
from masonite.view import View

from app.helpers.mix import mix


class CustomHelpersProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        pass

    def boot(self, view: View):
        """Add custom helper functions to Masonite."""
        view.share({"mix": mix})
