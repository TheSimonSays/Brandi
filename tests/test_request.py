import pytest
from brandi import Brandi, html, json, text, template_string
from webtest import TestApp
from json import dumps


def init_app(app_name: str) -> TestApp:
    brandi = Brandi(app_name)
    app = TestApp(brandi)
    return brandi, app


def test_request_get_args():
    brandi, app = init_app('test_request_args_app')

    @brandi.route('/args')
    def get_args(request):
        return text('', 200)

    response = app.get('/args', params='name=Brandi')
    
    assert response.status_int == 200
    assert dict(response.request.params) == {'name': 'Brandi'}
