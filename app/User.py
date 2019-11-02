"""User Model."""
from app.UserOptions import UserOptions
from app.auth.MustVerifyEmail import MustVerifyEmail
from config.database import Model
from orator.orm import has_one

class User(Model, MustVerifyEmail):
    """User Model."""

    __fillable__ = ["name", "email", "password", "verified_at"]

    __auth__ = "email"

    @has_one
    def options(self):
        return UserOptions
