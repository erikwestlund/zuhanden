from masonite.auth import Auth
from masonite.helpers import config
from masonite.managers import MailManager
from masonite.request import Request
from masonite.validation import Validator

from app.User import User
from app.auth.MustVerifyEmail import MustVerifyEmail
from app.helpers.return_with_errors import return_with_errors
from app.inertia.InertiaResponse import InertiaResponse


class SignUpController:
    def show(self, request: Request, inertia: InertiaResponse):

        if request.user():
            request.session.flash("warning", "You are already logged in.")
            return request.redirect("/")

        return inertia.render("UserSignUp")

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
            validate.not_in_database(
                "email",
                table="users",
                column="email",
                messages={"email": "This email address is already registered"},
            ),
            validate.confirmed("password"),
            validate.length(
                "password",
                min=config("auth.password_min_length"),
                max=config("auth.password_max_length"),
            ),
        )

        if errors:
            return return_with_errors(errors)

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
                "success", "Your account has been successfully created. Check your email to verify your email address.",
            )
            return request.redirect("/")
