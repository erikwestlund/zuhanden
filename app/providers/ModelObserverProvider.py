"""A ModelObserverProvider Service Provider."""

from masonite.provider import ServiceProvider

from app import User
from app.model_observers.UserObserver import UserObserver


class ModelObserverProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        pass

    def boot(self):
        """Boots services required by the container."""
        User.observe(UserObserver())


jmgg;g;/reversed() V,  mx k
