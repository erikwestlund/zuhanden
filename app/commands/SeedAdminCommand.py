"""A SeedAdminCommand Command."""
from cleo import Command
from masonite.helpers import password
from app.User import User

class SeedAdminCommand(Command):
    """
    Seeds the administrator user.

    zuhanden:seed_admin
    """

    def handle(self):
        email = self.ask('What is your email?')
        name = self.ask('What is your name?')
        password = self.ask('Provide a password.')

        from wsgi import container
        validator = container.make('Validator')

        errors = self.validate_input(email, name, validator)

        if errors:
            self.print_errors(errors)
        else:
            user = User.create(
                email=email,
                name=name,
                password=password(password)
            )
            self.line('<info>User generated successfully.</info>')

    def print_errors(self, errors):
        for error in errors:
            for message in errors[error]:
                self.error(message)

    def validate_input(self, email, name, validator):
        errors = validator.validate({
            'email': email or '',
            'name': name or ''
        },
            validator.required(['email', 'name']),
            validator.email(['email']),
        )
        return errors

