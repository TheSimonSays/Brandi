import typing as t
from brandi.config import Config
from brandi.context import Context
from brandi.request_handler import RequestHandler
from brandi.route import Route
from brandi.route_map import RouteMap
from brandi.types import DefaultConfig


class App:
    """
    Parent app class
    """
    static_folder: str
    templates_folder: str
    config: Config
    context: Context
    request_handler: RequestHandler
    routes_map: RouteMap

    def configure_app(self, defaults: t.Optional[DefaultConfig]) -> None:
        """
        Set defaul config to app
        :params default: default dict configuration
        """
        self.config = Config(defaults)

    def init_context(self, obj: object) -> None:
        """
        A temporary method that puts the current class object into context
        :param obj: instance of Brandi class
        """
        self.context = Context.init_curent_app_context(obj)

    def init_request_handler(self, environ: dict, start_response: t.Any) -> None:
        """
        Set request handler
        :param environ: dict of wsgi environ
        :param start_response: point of entry mod_wsgi 
        """
        self.request_handler = RequestHandler(environ, start_response)

    def route(self, path: str, **args: t.Any) -> t.Callable:
        """
        Special decorator.
        Apends route to all routes list.
        :params path: path of the url
        :params args: keyword arguments, which may contain methods
        """
        def decorator(f: t.Callable) -> None:
            RouteMap.add_route(Route(path, f, args.get('methods', ['GET'])))
        return decorator
