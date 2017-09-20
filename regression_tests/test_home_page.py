from . import runner

from pages import HomePage

def test_home_title_loads(runner):
    home = HomePage(runner)
    home.go()
    assert 'My Cool Site' == home.get_title()

def test_home_has_default_message(runner):
    home = HomePage(runner)
    home.go()
    assert home.has_message("Bye, World!")

def test_home_has_blake_message(runner):
    home = HomePage(runner, path='/blake')
    home.go()
    assert home.has_message("Bye, blake!")

def test_home_click_link(runner):
    home = HomePage(runner)
    home.go()
    picture = home.click_picture_link()
    assert 'My Cool Picture' == picture.get_title()