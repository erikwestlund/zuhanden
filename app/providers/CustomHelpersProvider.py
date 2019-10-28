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

        builtins.error_response = error_response
        builtins.success_response = success_response

        view.share({"mix": mix})


def error_response(errors):
    from wsgi import container

    request = container.make("Request")
    request.status(422)
    return {"errors": errors}


def success_response(object):
    from wsgi import container

    request = container.make("Request")
    request.status(200)
    return {"success": True, "payload": object}
