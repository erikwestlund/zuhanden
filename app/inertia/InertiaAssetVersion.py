import hashlib

from masonite.helpers import config


class InertiaAssetVersion:
    def get(self):
        manifest = config("resources.public_path") + "/mix-manifest.json"

        hasher = hashlib.md5()
        with open(manifest, "rb") as manifest_file:
            buf = manifest_file.read()
            hasher.update(buf)
        return hasher.hexdigest()
