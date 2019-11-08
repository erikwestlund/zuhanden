import hashlib
import html
import json

from masonite.helpers import config


class InertiaResponse:
    def __init__(self, container):
        self.container = container
        self.request = self.container.make("Request")
        self.view = self.container.make("View")
        self.asset_version = self.container.make("InertiaAssetVersion").get()

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
            "version": self.get_version(),
        }

    def get_props(self, props):
        return props

    def get_component(self, component):
        return html.escape(component)

    def get_version(self):
        return self.asset_version
