"""A LoginController Module."""

from masonite.auth import Auth
from masonite.request import Request
from masonite.view import View

from app.inertia.InertiaResponse import InertiaResponse


class LoginController:
    """Login Form Controller."""

    def __init__(self):
        """LoginController Constructor."""
        pass

    def show(self, request: Request, inertia: InertiaResponse):
        if request.user():
            return request.redirect("/")
        return inertia.render("UserLogin")
        return view.render("users/login", {"hide_user_actions": True})

    def login(self, request: Request, auth: Auth):
        user = auth.login(request.input("email"), request.input("password"))

        if user:
            request.session.flash("success", "You have been logged in.")
            return success_response({"email": user.email})

        return error_response(
            {"password": ["We could not validate these credentials. Please try again."]}
        )

    def logout(self, request: Request, auth: Auth):
        if not request.user():
            request.session.flash("warning", "You are already logged out.")
            return request.redirect("/")

        auth.logout()
        request.session.flash("success", "You have been logged out.")
        return request.redirect("/")
