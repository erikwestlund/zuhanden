def return_with_errors(errors):
    from wsgi import container

    clean_errors = {}
    for error in errors:
        if isinstance(errors[error], list):
            clean_errors.update({error: errors[error]})
        else:
            clean_errors.update({error: [errors[error]]})

    request = container.make("Request")
    return request.back().with_errors(clean_errors)
