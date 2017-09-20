class BasePage():

    base_url = 'http://localhost:5000'

    def __init__(self, browser):
        self.browser = browser

    def get_title(self):
        return self.browser.title