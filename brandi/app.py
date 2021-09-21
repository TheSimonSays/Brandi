import typing as t
from brandi.config import Config
from brandi.context import Context
from brandi.request_handler import RequestHandler
from brandi.route import Route
from brandi.route_map import RouteMap
from brandi.types import DefaultConfig


class App:
    static_folder: str
    templates_folder: str
    config: Config
    context: Context
    request_handler: RequestHandler
    routes_map: RouteMap

    def configure_app(self, defaults: t.Optional[DefaultConfig]) -> None:
        self.config = Config(defaults)

    def init_context(self, obj: object) -> None:
        self.context = Context.init_curent_app_context(obj)

    def init_request_handler(self, environ: dict, start_response: t.Any) -> None:
        self.request_handler = RequestHandler(environ, start_response)

    def route(self, path: str, **args: t.Any) -> t.Callable:
        def decorator(f: t.Callable) -> None:
            RouteMap.add_route(Route(path, f, args.get('methods', ['GET'])))
        return decorator
