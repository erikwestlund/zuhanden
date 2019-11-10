import html
import json

from app.inertia.InertiaAssetVersion import inertia_asset_version
from masonite.helpers import compact


class InertiaResponse:
    def __init__(self, container):
        self.container = container
        self.request = self.container.make("Request")
        self.view = self.container.make("View")

    def render(self, component, props={}):
        page_data = self.get_page_data(component, props)

        if self.request.is_inertia:
            return json.dumps(page_data)

        return self.view("app", {"page": html.escape(json.dumps(page_data))})

    def get_page_data(self, component, props):
        return {
            "component": self.get_component(component),
            "props": self.get_props(props),
            "url": self.request.path,
            "version": inertia_asset_version(),
        }

    def get_props(self, props):
        props.update({"errors": self.get_errors()})
        props.update({"auth": self.get_auth()})
        props.update({"messages": self.get_messages()})
        return props

    def get_auth(self):
        user = self.request.user()

        if not user:
            return {"user": None}

        return {"user": {"email": user.email, "name": user.name}}

    def get_messages(self):
        return {
            "success": (self.request.session.get("success") or ""),
            "error": (self.request.session.get("error") or ""),
            "danger": (self.request.session.get("danger") or ""),
            "warning": (self.request.session.get("warning") or ""),
            "info": (self.request.session.get("info") or "")
        }

    def get_errors(self):
        return self.request.session.get("errors") or {}

    def get_component(self, component):
        return html.escape(component)
