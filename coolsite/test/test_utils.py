from coolsite import utils


def test_say_hello_empty():
    assert utils.say_hello() == 'Hello!'


def test_say_hello_blake():
    assert utils.say_hello('Blake') == 'Hello, Blake!'
