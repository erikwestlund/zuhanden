"""Role Model."""
from orator.orm import belongs_to_many, has_many

from config.database import Model


class Role(Model):
    """Role Model."""

    @belongs_to_many
    def permissions(self):
        from app.Permission import Permission

        return Permission

    @belongs_to_many
    def users(self):
        from app.User import User

        return User
