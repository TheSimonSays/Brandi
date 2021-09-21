import typing as t
from brandi.request import Request
from brandi.route_map import RouteMap
from brandi.status import HTTP_STATUS


class RequestHandler:
    def __init__(self, environ: dict, start_response: t.Any) -> None:
        self.environ = environ
        self.start_response = start_response

    def route_not_found(self):
        self.start_response(HTTP_STATUS[404], [])
        return b''

    def method_not_allowed(self):
        self.start_response(HTTP_STATUS[405], [])
        return b''

    def request_dispatch(self):
        request = Request(self.environ)
        for route in RouteMap.routes:
            route_params = route.route_params
            if not route_params:
                if request.path == route.path:
                    if request.method not in route.methods:
                        return self.method_not_allowed()
                    response = route.view(request)
                    self.start_response(response.status, response.headers)
                    return [response.body]
            else:
                url_pattern = route_params.pattern
                url_match = url_pattern.match(request.path)
                if url_match:
                    if request.method in route.methods:
                        response = route.view(route_params.bind_type(url_match.group(1)), request)
                        self.start_response(response.status, response.headers)
                        return [response.body]
                    else:
                        return self.route_not_found()
        return self.route_not_found()
