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
        builtins.abort_404 = abort_404
        builtins.abort_403 = abort_403

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


def abort(status_code):
    from wsgi import container
    from masonite.response import Response

    response = container.make(Response)
    view = container.make("View")

    return response.view(view('errors/{}'.format(status_code)), status=status_code)


def abort_403():
    return abort(403)


def abort_404():
    return abort(404)
