"""A Helper Service Provider."""

import builtins

from masonite.provider import ServiceProvider
from masonite.view import View

from app.helpers.abort import abort_404, abort_403
from app.helpers.error_json_response import error_json_response
from app.helpers.mix import mix
from app.helpers.success_json_response import success_json_response


class CustomHelpersProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        pass

    def boot(self, view: View):
        """Add custom helper functions to Masonite."""

        builtins.error_response = error_json_response
        builtins.success_response = success_json_response
        builtins.abort_404 = abort_404
        builtins.abort_403 = abort_403

        view.share({"mix": mix})
