"""User Model."""
from orator.orm import belongs_to_many

from app.auth.MustVerifyEmail import MustVerifyEmail
from config.database import Model


class User(Model, MustVerifyEmail):
    """User Model."""

    __fillable__ = ["name", "email", "password", "options", "verified_at"]

    __auth__ = "email"

    @belongs_to_many
    def roles(self):
        from app.Role import Role
        return Role
