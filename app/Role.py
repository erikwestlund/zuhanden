"""Role Model."""
from orator.orm import belongs_to_many

from config.database import Model


class Role(Model):
    """Role Model."""

    @belongs_to_many
    def permissions(self):
        from app.Permission import Permission
        return Permission
