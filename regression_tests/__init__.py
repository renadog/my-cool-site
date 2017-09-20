from selenium import webdriver
import pytest

@pytest.fixture(scope='module')
def runner(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.set_page_load_timeout(5)

    def fin():
        driver.quit()

    request.addfinalizer(fin)

    return driver