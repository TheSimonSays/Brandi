from brandi.status import HTTP_STATUS
import typing as t
from brandi.types import Headers
from brandi.wrappers import cached_property
from json import dumps
from brandi.template import render_template, render_template_string


class Response:
    http_version = '1.1'

    def __init__(
        self,
        body: t.Any = '',
        status: int = 200,
        content_type: str = 'text/html',
        headers: t.Optional[Headers] = None
    ) -> None:
        self.charset = 'utf-8'
        self._body = body
        self.status = HTTP_STATUS.get(status)
        self.content_type = content_type
        self._headers = headers

    @cached_property
    def headers(self):
        headers = [
            ('Content-type', self.content_type),
            ('Charset', self.charset)
        ]
        if self._headers:
            headers += list(self._headers.items())
        return headers

    @cached_property
    def body(self):
        return self._body.encode(self.charset)


def template(template: str, status: int = 200, content_type: str = 'text/html', headers: Headers = None, **context) -> Response:    # noqa: E501
    return Response(
        render_template(template, **context),
        status,
        content_type,
        headers
    )


def template_string(html_string: str, status: int = 200, content_type: str = 'text/html', headers: Headers = None, **context) -> Response:  # noqa: E501
    return Response(
        render_template_string(html_string, **context),
        status,
        content_type,
        headers
    )


def json(body: dict, status: int = 200, content_type: str = 'application/json', headers: Headers = None) -> Response:
    return Response(dumps(body), status, content_type, headers)


def html(body: t.Any, status: int = 200, content_type: str = 'text/html', headers: Headers = None) -> Response:
    return Response(body, status, content_type, headers)


def text(body: t.Any, status: int = 200, content_type: str = 'text/plain', headers: Headers = None) -> Response:
    return Response(body, status, content_type, headers)
