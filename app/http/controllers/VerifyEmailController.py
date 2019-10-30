import datetime

from masonite.auth import Auth
from masonite.auth.Sign import Sign
from masonite.managers import MailManager
from masonite.request import Request
from masonite.view import View

from app.auth.MustVerifyEmail import MustVerifyEmail


class VerifyEmailController:
    def verify_show(self, request: Request, view: View):

        if not request.user():
            request.session.flash(
                "warning", "You must be logged in verify your email address."
            )
            return request.redirect("/login")

        return view.render("users/email-verification")

    def confirm_email(self, request: Request, view: View, auth: Auth):
        sign = Sign()
        token = sign.unsign(request.param("id"))

        if token is not None:
            tokenParts = token.split("::")
            if len(tokenParts) > 1:
                user = auth.auth_model.find(tokenParts[0])

                if user.verified_at is None:
                    timestamp = datetime.datetime.fromtimestamp(float(tokenParts[1]))
                    now = datetime.datetime.now()
                    timestamp_plus_10 = timestamp + datetime.timedelta(minutes=10)

                    if now < timestamp_plus_10:
                        user.verified_at = datetime.datetime.now()
                        user.save()

                        return view.render("users/email-verification-success")

        return view.render("users/email-verification-error")

    def send_verify_email(self, manager: MailManager, request: Request):
        user = request.user()

        if isinstance(user, MustVerifyEmail):
            user.verify_email(manager, request)

        request.session.flash("success", "A verification email has been sent.")
        return request.redirect("/")
