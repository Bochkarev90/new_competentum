class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = driver.current_url
