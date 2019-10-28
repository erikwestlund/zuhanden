"""The RegisterController Module."""
from masonite.validation import Validator

from config import application, auth as auth_config
from masonite.auth import Auth
from masonite.request import Request
from masonite.view import View
from masonite.auth import MustVerifyEmail
from masonite.managers import MailManager


class RegisterController:
    """The RegisterController class."""

    def __init__(self):
        """The RegisterController Constructor."""
        pass

    def show(self, request: Request, view: View):
        """Show the registration page.

        Arguments:
            Request {masonite.request.request} -- The Masonite request class.

        Returns:
            masonite.view.View -- The Masonite View class.
        """

        if auth():
            request.session.flash("warning", "You are already logged in.")
            return request.redirect("/")

        return view.render("users/register")

    def store(
        self,
        request: Request,
        mail_manager: MailManager,
        auth: Auth,
        validate: Validator,
    ):
        """Register the user with the database.

        Arguments:
            request {masonite.request.Request} -- The Masonite request class.

        Returns:
            masonite.request.Request -- The Masonite request class.
        """

        errors = request.validate(
            validate.required(["name", "email", "password"]),
            validate.email("email"),
            validate.confirmed("password"),
        )

        if errors:
            request.status(422)
            return {"errors": errors}
        else:
            user = auth.register(
                {
                    "name": request.input("name"),
                    "password": request.input("password"),
                    "email": request.input("email"),
                }
            )

            if isinstance(user, MustVerifyEmail):
                user.verify_email(mail_manager, request)

            # Login the user
            if auth.login(request.input("email"), request.input("password")):
                request.session.flash(
                    "success",
                    "Your account has been created and you have been logged in!",
                )
                return request.redirect("/")
