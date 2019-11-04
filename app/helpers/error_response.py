def error_response(errors):
    from wsgi import container

    request = container.make("Request")
    request.status(422)
    return {"errors": errors}
