"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [Get("/", "InertiaTestController@show").name("index")]

ROUTES = ROUTES + [
    Get().route("/inertia", "InertiaTestController@show"),
    Get().route("/login", "LoginController@show").name("login"),
    Post().route("/login", "LoginController@login"),
    Get().route("/logout", "LoginController@logout").name("logout"),
    Get().route("/register", "RegisterController@show").name("register"),
    Post().route("/register", "RegisterController@store"),
    Get()
    .route("/users/verify-email", "VerifyEmailController@verify_show")
    .name("verify"),
    Get().route("/users/verify-email/send", "VerifyEmailController@send_verify_email"),
    Get().route(
        "/users/verify-email/@id:signed", "VerifyEmailController@confirm_email"
    ),
    Get()
    .route("/users/reset-password", "PasswordController@reset_form")
    .name("forgot.password"),
    Post().route("/users/reset-password", "PasswordController@send"),
    Get()
    .route("/users/reset-password/@token", "PasswordController@reset")
    .name("password.reset"),
    Post().route("/users/reset-password/@token", "PasswordController@update"),
]
