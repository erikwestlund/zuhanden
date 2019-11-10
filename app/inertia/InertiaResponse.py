import html
import json

from app.inertia.InertiaAssetVersion import inertia_asset_version


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
            "version": inertia_asset_version()
        }

    def get_props(self, props):
        props.update({"errors": (self.request.session.get('errors') or {})})
        props.update({"auth": self.get_auth()})
        return props

    def get_auth(self):
        user = self.request.user()

        if not user:
            return {
                "user": None
            }

        return {
            "user": {
                "email": user.email,
                "name": user.name
            }
        }

    def get_component(self, component):
        return html.escape(component)
