import json
from masonite.helpers import config


def mix(filename):
    manifest = config("resources.public_path") + "/mix-manifest.json"

    with open(manifest) as file:
        data = json.load(file)

    return "/static" + data[filename]
