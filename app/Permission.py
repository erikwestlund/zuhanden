"""Permission Model."""
from orator.orm import belongs_to_many

from config.database import Model


class Permission(Model):
    """Permission Model."""

    @belongs_to_many
    def roles(self):
        from app.Role import Role
        return Role
