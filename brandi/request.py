import re
from brandi.wrappers import cached_property
from brandi.types import JSONTyped
from requests_toolbelt.multipart import decoder
from json import loads, JSONDecodeError
from urllib.parse import urlparse, parse_qs, unquote


class Request:
    def __init__(self, environ: dict) -> None:
        self.__environ = environ
        self._json: JSONTyped = {}
        self._form: JSONTyped = {}
        self._content_type: str = ''
        self._body: bytes = b''

    @property
    def method(self):
        return self.__environ.get('REQUEST_METHOD')

    @property
    def schema(self):
        return self.__environ.get('wsgi.url_scheme', 'http')

    @property
    def path(self):
        return urlparse(self.__environ.get('PATH_INFO', '')).path

    @property
    def content_type(self):
        type_ = self.__environ.get('CONTENT_TYPE')
        if type_:
            self._content_type = type_
        return self._content_type

    @property
    def args(self):
        return parse_qs(urlparse(self.__environ.get('RAW_URI', '')).query)

    @property
    def body(self):
        response = self.__environ.get('wsgi.input').read()
        if response is not None and response != b'':
            self._body = response
        return self._body

    @cached_property
    def json(self):
        response = unquote(self.__environ.get('wsgi.input').readline().decode().strip())
        try:
            self._json = loads(response)
        except JSONDecodeError:
            pass
        return self._json

    @property
    def form(self):
        if self.content_type == 'application/json':
            self._form = self.json
        else:
            parts = decoder.MultipartDecoder(self.body, self.content_type).parts
            for part in parts:
                header = part.headers.get(b'Content-Disposition').decode().split('; ')[-1]
                self._form[re.findall(r'=(.*)', header)[0].replace('"', '')] = part.text
        return self._form
