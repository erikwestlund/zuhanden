from masonite.provider import ServiceProvider
from masonite.validation import Validator

from app.rules.not_in_database import not_in_database


class RuleProvider(ServiceProvider):
    """Provides Rules To The Service Container."""

    wsgi = False

    def boot(self, validator: Validator):
        """Registers custom rules
        """

        validator.register(not_in_database)
