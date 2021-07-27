import re
from yaml import load, FullLoader
from collections.abc import Mapping


class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"

    def load(self, cls, string):
        (_, fm, content) = __regex.split(string, 2)
        load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return


class __regex: re.compile(__delimeter, re.MULTILINE)
