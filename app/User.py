"""User Model."""

from config.database import Model


class User(Model):
    """User Model."""

    __fillable__ = ['name', 'email', 'password', 'verified_at']

    __auth__ = 'email'
