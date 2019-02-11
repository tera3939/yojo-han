import typing as t


# https://github.com/python/typing/issues/182#issuecomment-186306678
_JSONType_0 = t.Union[str, int, float, bool, None, t.Dict[str, t.Any], t.List[t.Any]]
_JSONType_1 = t.Union[str, int, float, bool, None, t.Dict[str, _JSONType_0], t.List[_JSONType_0]]
_JSONType_2 = t.Union[str, int, float, bool, None, t.Dict[str, _JSONType_1], t.List[_JSONType_1]]
_JSONType_3 = t.Union[str, int, float, bool, None, t.Dict[str, _JSONType_2], t.List[_JSONType_2]]
Json = t.Union[str, int, float, bool, None, t.Dict[str, _JSONType_3], t.List[_JSONType_3]]
