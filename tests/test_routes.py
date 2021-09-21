import pytest
from brandi import Brandi, text
from webtest import TestApp


def init_app(app_name: str) -> TestApp:
    brandi = Brandi(app_name)
    app = TestApp(brandi)
    return brandi, app

def test_routes():
    brandi, app = init_app('test_routes_app')

    @brandi.route('/')
    def main_route(request):
        return text('main', 200)

    response = app.get('/')
    assert response.status == '200 OK'


def test_route_params():
    brandi, app = init_app('test_route_params_app')

    @brandi.route('/users/<int:user_id>')
    def main_route(user_id, request):
        return text(str(user_id), 200)

    response = app.get('/users/1')
    assert response.status == '200 OK'
    assert '1' in response