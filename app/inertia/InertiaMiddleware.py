from masonite.request import Request
from masonite.response import Response

from app.inertia.InertiaAssetVersion import InertiaAssetVersion


class InertiaMiddleware:
    """Inertia Middleware to check whether this is an Inertia request."""

    def __init__(
        self, request: Request, response: Response, asset_version: InertiaAssetVersion
    ):
        self.request = request
        self.response = response
        self.asset_version = asset_version.get()

    def before(self):
        self.request.is_inertia = self.request.header("HTTP_X_INERTIA")

        if (
            self.request.is_inertia
            and self.request.method == "GET"
            and self.request.header("HTTP_X_INERTIA_VERSION") != self.asset_version
        ):
            self.request.header("X-Inertia-Location", self.request.path)
            return self.response.view("", status=409)

    def after(self):
        if self.request.is_inertia:
            self.request.header("Vary", "Accept")
            self.request.header("X-Inertia", True)
            self.request.header("X-Inertia-Version", self.asset_version)
