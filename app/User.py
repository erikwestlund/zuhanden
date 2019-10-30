"""User Model."""
from masonite.auth import MustVerifyEmail

from config.database import Model


class User(Model, MustVerifyEmail):
    """User Model."""

    __fillable__ = ["name", "email", "password", "verified_at"]

    __auth__ = "email"
