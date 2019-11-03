"""A ModelObserverProvider Service Provider."""

from masonite.provider import ServiceProvider

from app.User import User
from app.model_observers.UserObserver import UserObserver


class ModelObserverProvider(ServiceProvider):
    """Register Orator model observers."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        pass

    def boot(self):
        User.observe(UserObserver())
