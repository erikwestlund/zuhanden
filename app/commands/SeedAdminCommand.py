"""A SeedAdminCommand Command."""
from cleo import Command
import pendulum

from app.User import User
from masonite.helpers import password as hash_bcrypt


class SeedAdminCommand(Command):
    """
    Seeds the administrator user.

    zuhanden:seed_admin
    """

    def handle(self):
        self.line("<info>Add an administrator to the database.</info>")

        email = self.ask("What is your email?")
        name = self.ask("What is your name?")
        password = self.secret("Provide a password.")

        errors = self.validate_input(email, name, password)

        if errors:
            self.print_errors(errors)
        else:
            user = User.create(
                email=email,
                name=name,
                password=hash_bcrypt(password),
                verified_at=pendulum.now(),
            )
            self.line("<info>User generated successfully.</info>")

    def print_errors(self, errors):
        for error in errors:
            for message in errors[error]:
                self.error(message)

    def validate_input(self, email, name, password):
        from wsgi import container

        validator = container.make("Validator")
        errors = validator.validate(
            {"email": email or "", "name": name or "", "password": password or ""},
            validator.required(["email", "name", "password"]),
            validator.email(["email"]),
        )

        users_with_email = User.where("email", email).count()

        if users_with_email >= 1:
            errors.update({"email_exists": ["This email already exists in database"]})

        return errors
