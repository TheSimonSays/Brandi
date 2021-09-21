import re
import typing as t


class RouteParams:
    def __init__(self, pattern: t.Optional[re.Pattern] = None, param_name: str = None, bind_type: t.Optional[type] = None) -> None:
        self.pattern = pattern
        self.param_name = param_name
        self.bind_type = bind_type


class Route:
    rules_types = {
        'string': (str, r'[^/]+'),
        'int': (int, r'\d+'),
    }

    def __init__(self, path: str, view: t.Callable, methods: t.List[str]) -> None:
        self.path = path
        self.view = view
        self.methods = methods
        self.params = {}
        self.route_params = self.add_route_params()

    def add_route_params(self) -> RouteParams:
        if ':' in self.path:
            url_params = re.search('<(.*)>', self.path)
            if url_params:
                path = re.search(r'(\/.*\/)', self.path).group(0)
                param_type, param_name = url_params.group(1).split(':')
                type_, re_pattern = self.rules_types.get(param_type, 'string')
                pattern = re.compile(rf'^{path}({re_pattern})$')
                return RouteParams(pattern, param_name, type_)
