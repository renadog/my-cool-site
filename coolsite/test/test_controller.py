import pytest
from coolsite import app, controller  # noqa: F401


@pytest.fixture(scope='module')
def test_app(request):
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    return app.test_client()


def test_name_controller_empty(test_app):
    result = test_app.get('/')
    assert result.status_code == 200
    assert 'Bye, World!' in result.data


def test_name_controller_blake(test_app):
    result = test_app.get('/blake')
    assert result.status_code == 200
    assert 'Bye, blake!' in result.data


def test_picture_controller_empty(test_app):
    result = test_app.get('/picture/')
    assert result.status_code == 200


def test_picture_controller_redirect(test_app):
    result = test_app.get('/picture')
    assert result.status_code == 301


def test_picture_controller_exists(test_app):
    result = test_app.get('/picture/rena')
    assert result.status_code == 200
    assert 'couldn\'t find the requested image, here take this!' not in result.data


def test_picture_controller_does_not_exists(test_app):
    result = test_app.get('/picture/blake')
    assert result.status_code == 200
    assert 'couldn\'t find the requested image, here take this!' in result.data
