"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [Get("/", "IndexController@show").name("index")]

ROUTES = ROUTES + [
    Get().route("/users/sign-in", "SignInController@show").name("sign_in"),
    Post().route("/users/sign-in", "SignInController@sign_in"),
    Get().route("/users/sign-out", "SignInController@sign_out").name("sign_out"),
    Get().route("/users/register", "RegisterController@show").name("register"),
    Post().route("/users/register", "RegisterController@store"),
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
