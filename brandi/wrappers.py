import typing as t


class cached_property:
    def __init__(self, function: t.Callable) -> None:
        self.function = function

    def __get__(self, instance: object, cls: t.Optional[object] = None) -> t.Any:
        result = instance.__dict__[self.function.__name__] = self.function(instance)
        return result
