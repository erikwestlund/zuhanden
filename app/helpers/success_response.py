def success_response(object):
    from wsgi import container

    request = container.make("Request")
    request.status(200)
    return {"success": True, "payload": object}
