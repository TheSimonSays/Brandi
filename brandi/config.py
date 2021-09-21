import typing as t
from brandi.types import DefaultConfig


class Config(t.MutableMapping):
    def __init__(self, defaults: t.Optional[DefaultConfig] = None) -> None:
        self.config: t.Dict[str, t.Any] = {}
        if defaults:
            self.config = defaults

    def from_object(self, obj: object) -> None:
        for key in filter(lambda x: x.isupper(), dir(obj)):
            self.config[key] = getattr(obj, key)

    def from_dict(self, d_obj: t.Dict[str, t.Any]) -> None:
        for key, value in d_obj.items():
            self.config[key] = value

    def __getitem__(self, key: str, default: t.Optional[t.Any] = None) -> t.Any:
        return self.config.get(key, default)

    def __setitem__(self, key: str, value: t.Any) -> None:
        self.config[key] = value

    def __delitem__(self, value: t.Any) -> None:
        del self.config[value]

    def __len__(self) -> int:
        return len(self.config)

    def __iter__(self) -> t.Iterator:
        return iter(self.config)
