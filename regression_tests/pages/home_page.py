import time
from regression_tests.pages.picture_page import PicturePage
from regression_tests.pages.base_page import BasePage

class HomePage(BasePage):

    path = '/'

    def __init__(self, browser, path=None):
        self.browser = browser
        if path:
            self.path = path

    def go(self):
        self.browser.get(self.base_url+self.path)

    def has_message(self, message):
        return self.browser.find_element_by_id('message').text == message

    def click_picture_link(self):
        picture_link = self.browser.find_element_by_id('next-page')
        picture_link.click()

        return PicturePage(self.browser)