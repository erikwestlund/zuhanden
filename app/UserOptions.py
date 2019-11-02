"""Setting Model."""

from config.database import Model


class UserOptions(Model):
    """Setting Model."""

    __fillable__ = ["user_id", "options"]
