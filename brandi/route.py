import typing as t


class Route:
    def __init__(self, path: str, view: t.Callable, methods: t.List[str]) -> None:
        self.path = path
        self.view = view
        self.methods = methods
