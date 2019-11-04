def user_can(permission):
    def decorator(function):
        def wrapper(*args, **kwargs):
            from wsgi import container

            request = container.make("Request")

            user = request.user()

            if not user:
                return abort_403()
            elif not user.can(permission):
                return abort_403()

            return container.resolve(function)

        return wrapper

    return decorator
