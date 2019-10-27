"""A CommandsProvider Service Provider."""

from masonite.provider import ServiceProvider

from app.commands.SeedAdminCommand import SeedAdminCommand


class CommandsProvider(ServiceProvider):
    """Provides commands To The Service Container."""

    wsgi = False

    def register(self):
        self.app.bind('SeedAdminCommand', SeedAdminCommand)

    def boot(self):
        pass
