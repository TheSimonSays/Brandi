import typing as t


# custom types

Headers = t.Mapping[str, t.Union[str, int]]
DefaultConfig = t.Dict[str, t.Any]
JSONTyped = t.Optional[t.Dict[t.Any, t.Any]]
