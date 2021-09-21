import typing as t
from brandi.request import Request
from brandi.route_map import RouteMap


class RequestHandler:
    def __init__(self, environ: dict, start_response: t.Any) -> None:
        self.environ = environ
        self.start_response = start_response

    def not_found(self):
        self.start_response('404', [])
        return b''

    def method_not_allowed(self):
        self.start_response('405', [])
        return b''

    def request_dispatch(self):
        request = Request(self.environ)
        for route in RouteMap.routes:
            if request.path == route.path:
                if request.method not in route.methods:
                    return self.method_not_allowed()
                response = route.view(request)
                self.start_response(response.status, response.headers)
                return [response.body]
        return self.not_found()
