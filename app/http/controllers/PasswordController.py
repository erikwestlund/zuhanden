"""A PasswordController Module."""

import uuid

from masonite import env, Mail, Session
from masonite.auth import Auth
from masonite.helpers import password as bcrypt_password, config
from masonite.request import Request
from masonite.validation import Validator
from masonite.view import View

from config.auth import AUTH


class PasswordController:
    """Password Controller."""

    reset_message = "We have sent directions on how to reset your password to the provided email. If you do not receive an email, try again."

    def reset_form(self, view: View):
        return view.render("users/password-reset-request")

    def reset(self, request: Request, auth: Auth):
        token = request.param("token")
        user = AUTH["model"].where("remember_token", token).first()
        if user:
            return view(
                "users/password-reset",
                {
                    "token": token,
                    "app": request.app().make("Application"),
                    "Auth": auth,
                },
            )

    def send(self, request: Request, session: Session, mail: Mail, validate: Validator):

        errors = request.validate(validate.required("email"), validate.email("email"))

        if errors:
            request.session.flash("error", errors)
            return request.back()

        email = request.input("email")
        user = AUTH["model"].where("email", email).first()

        if user:
            if not user.remember_token:
                user.remember_token = str(uuid.uuid4())
                user.save()

            link = "{}/users/reset-password/{}".format(
                request.environ["HTTP_HOST"], user.remember_token
            )

            mail.subject(
                "{}: Reset Your Password".format(config("application.name"))
            ).template(
                "users/password-reset-email", {"name": user.name, "link": link}
            ).to(
                user.email
            ).send()

        session.flash("success", self.reset_message)

        return request.redirect("/")

    def update(self, request: Request, validate: Validator):

        errors = request.validate(
            validate.required("password"),
            validate.confirmed("password"),
            validate.length(
                "password",
                min=config("auth.password_min_length"),
                max=config("auth.password_max_length"),
            ),
        )

        if errors:
            request.session.flash("error", errors)
            return request.back()

        user = AUTH["model"].where("remember_token", request.param("token")).first()
        if user:
            user.password = bcrypt_password(request.input("password"))
            user.remember_token = None
            user.save()

            if request.user():
                auth.sign_out()

            request.session.flash(
                "success", "Your password has been reset. Login below."
            )
            return request.redirect("/users/sign-in")
