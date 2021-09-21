import pytest
from brandi import Brandi, html, json, text
from webtest import TestApp


def init_app(app_name: str) -> TestApp:
    brandi = Brandi(app_name)
    app = TestApp(brandi)
    return brandi, app


def test_text_response():
    brandi, app = init_app('test_text_response_app')

    @brandi.route('/text')
    def get_text(request):
        return text('simple text', 200)

    response = app.get('/text')
    assert response.status_int == 200 
    assert response.content_type == 'text/plain'
    assert 'simple text' in response


def test_html_response():
    brandi, app = init_app('test_html_response_app')

    @brandi.route('/html')
    def get_html(request):
        return html('<span>span tag</span>', 200)

    response = app.get('/html')
    assert response.status_int == 200 
    assert response.content_type == 'text/html'
    response.mustcontain('<span>')
    assert 'span' in response
