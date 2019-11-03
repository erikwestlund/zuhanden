"""A CommandsProvider Service Provider."""

from masonite.provider import ServiceProvider

from app.commands.CreateAdministratorCommand import CreateAdministratorCommand


class CommandsProvider(ServiceProvider):
    """Provides commands To The Service Container."""

    wsgi = False

    def register(self):
        self.app.bind("CreateAdministratorCommand", CreateAdministratorCommand)

    def boot(self):
        pass
