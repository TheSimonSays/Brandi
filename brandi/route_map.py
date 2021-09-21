import typing as t
from brandi.route import Route


class RouteMap:
    routes: t.List[Route] = []

    @classmethod
    def add_route(cls, route: Route) -> None:
        cls.routes.append(route)
