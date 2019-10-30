"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [Get("/", "IndexController@show").name("index")]

ROUTES = ROUTES + [
    # Get().route("/login", "LoginController@show").name("login"),
    # Post().route("/login", "LoginController@login"),
    # Get().route("/logout", "LoginController@logout").name("logout"),
    # Get().route("/register", "RegisterController@show").name("register"),
    # Post().route("/register", "RegisterController@store"),
    # Get().route("/email/verify", "ConfirmController@verify_show").name("verify"),
    # Get().route("/email/verify/send", "ConfirmController@send_verify_email"),
    # Get().route("/email/verify/@id:signed", "ConfirmController@confirm_email"),
    # Get()
    # .route("/users/reset-password", "PasswordController@reset_form")
    # .name("forgot.password"),
    # Post().route("/users/reset-password", "PasswordController@send"),
    # Get()
    # .route("/users/reset-password/@token", "PasswordController@reset")
    # .name("password.reset"),
    # Post().route("/users/reset-password/@token", "PasswordController@update"),
]
