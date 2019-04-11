class BasePage:
    url = ''

    def __init__(self, driver):
        self.driver = driver

    def save_url(self):
        self.url = self.driver.current_url
