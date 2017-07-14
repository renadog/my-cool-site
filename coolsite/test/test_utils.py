from coolsite import utils


def test_say_hello_empty():
    assert utils.say_hello() == 'Bye!'


def test_say_hello_blake():
    assert utils.say_hello('Blake') == 'Bye, Blake!'
