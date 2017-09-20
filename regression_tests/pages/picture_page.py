from regression_tests.pages.base_page import BasePage

class PicturePage(BasePage):

    path = '/picture/'

    def __init__(self, browser, path=None):
        self.browser = browser
        if path:
            self.path = path

    def go(self):
        self.browser.get(self.base_url+self.path)
