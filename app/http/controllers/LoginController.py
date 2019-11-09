"""A LoginController Module."""

from masonite.auth import Auth
from masonite.request import Request
from masonite.validation import Validator
from masonite.view import View

from app.helpers.return_with_errors import return_with_errors
from app.inertia.InertiaResponse import InertiaResponse


class LoginController:
    """Login Form Controller."""

    def show(self, request: Request, inertia: InertiaResponse):
        if request.user():
            return request.redirect("/")
        return inertia.render("UserLogin")

    def login(self, inertia: InertiaResponse, request: Request, auth: Auth, validate: Validator):
        errors = request.validate(
            validate.required(['email', 'password']),
            validate.email('email'),
        )

        if errors:
            return return_with_errors(errors)

        user = auth.login(request.input("email"), request.input("password"))

        if not user:
            return return_with_errors({"password": "These credentials could not be verified"})

        request.session.flash("success", "You have been logged in.")
        return request.redirect("/")


    def logout(self, request: Request, auth: Auth):
        if not request.user():
            request.session.flash("warning", "You are already logged out.")
            return request.redirect("/")

        auth.logout()
        request.session.flash("success", "You have been logged out.")
        return request.redirect("/")
