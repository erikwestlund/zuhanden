"""Verify Email Module."""

import time

from masonite.auth.Sign import Sign
from masonite.helpers import config


class MustVerifyEmail:
    """Class send a user verification email. Modified from class packaged in masonite.users.
    """

    def verify_email(self, mail_manager, request):
        """Sends email for user verification

        Arguments:
            mail_manager {masonite.managers.MailManager} -- Masonite mail manager class.
            request {masonite.request.Request} -- Masonite request class.
        """
        mail = mail_manager.helper()
        sign = Sign()

        token = sign.sign("{0}::{1}".format(self.id, time.time()))
        link = "{0}/users/verify-email/{1}".format(request.environ["HTTP_HOST"], token)

        mail.to(self.email).template(
            "users/email-verification-email",
            {"name": self.name, "email": self.email, "link": link},
        ).subject("{0}: Confirm Your Email".format(config("application.name"))).send()
