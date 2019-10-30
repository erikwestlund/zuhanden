from masonite.validation import Validator

from app.auth.MustVerifyEmail import MustVerifyEmail
from config import application, auth as auth_config
from masonite.auth import Auth
from masonite.request import Request
from masonite.view import View
from masonite.managers import MailManager

from app.User import User


class RegisterController:
    def show(self, request: Request, view: View):

        if auth():
            request.session.flash("warning", "You are already logged in.")
            return request.redirect("/")

        return view.render("users/register", {"hide_user_actions": True})

    def store(
        self,
        request: Request,
        mail_manager: MailManager,
        auth: Auth,
        validate: Validator,
    ):

        errors = request.validate(
            validate.required(["name", "email", "password"]),
            validate.email("email"),
            validate.confirmed("password"),
        )

        if errors:
            return error_response(errors)
        else:
            auth.register(
                {
                    "name": request.input("name"),
                    "password": request.input("password"),
                    "email": request.input("email"),
                }
            )

            user = User.where("email", request.input("email")).first()

            if isinstance(user, MustVerifyEmail):
                user.verify_email(mail_manager, request)

            # Login the user
            if auth.login(user.email, request.input("password")):
                request.session.flash(
                    "success",
                    "Your account has been created and you have been logged in!",
                )
                return success_response({"email": user.email})
