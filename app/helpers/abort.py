def abort(status_code):
    from wsgi import container
    from masonite.response import Response

    response = container.make(Response)
    view = container.make("View")

    return response.view(view("errors/{}".format(status_code)), status=status_code)


def abort_403():
    return abort(403)


def abort_404():
    return abort(404)
