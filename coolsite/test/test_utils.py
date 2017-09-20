from mock import patch
from coolsite import utils


def test_say_hello_empty():
    assert utils.say_hello() == 'Bye!'


def test_say_hello_blake():
    assert utils.say_hello('Blake') == 'Bye, Blake!'


@patch('coolsite.utils.url_for')
def test_build_image_path_for_name_casing(mock_url_for):
    mock_url_for.return_value = '/static/img/blake.png'
    assert utils.build_image_path_for('BlAkE') == '/static/img/blake.png'
    assert mock_url_for.called

@patch('coolsite.utils.url_for')
def test_build_image_path_for_None(mock_url_for):
    mock_url_for.return_value = '/static/img/blake.png'
    try:
        utils.build_image_path_for(None)
        assert False
    except AttributeError:
        assert True

def test_check_for_valid_path_none():
    assert utils.check_for_valid_path(None) is False


def test_check_for_valid_path_not_in_list():
    assert utils.check_for_valid_path('blake') is False


def test_check_for_valid_path_in_list():
    assert utils.check_for_valid_path('rena') is True


def test_check_for_valid_path_in_list_casing():
    assert utils.check_for_valid_path('ReNa') is True


@patch('random.choice')
def test_pick_random_name(mock_choice):
    mock_choice.return_value = 'rena'
    assert utils.pick_random_name() == 'rena'
    assert mock_choice.called
