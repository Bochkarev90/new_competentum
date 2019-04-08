from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.api import *
from input import xpath as x
import time


class Login:
    def __init__(self, browser_name, revel, login, password, book):
        self._platform = 'https://revel.pearson.com/#/start' if revel else 'http://etext.pearson.com/eplayer/login'
        self._login = login
        self._password = password
        self._browser = browser
        self._browser_name = browser_name
        self._book = book
        self.main_url = ''

    def driver(self):
        """
        Запускает драйвер браузера
        """

        # Если хром - добавляет английский язык браузеру
        if self._browser_name == 'chrome':
            chrome_options = Options()
            chrome_options.add_argument("--lang=en-us")
            driver = webdriver.Chrome(chrome_options=chrome_options)
            browser.set_driver(driver)
            
        # Запускает тот браузер, который указан в variables
        config.browser_name = self._browser_name

        # Запускает платформу (revel или etext)
        browser.open_url(self._platform)

    def login(self):
        """
        Запускает браузер, вводит логин и пароль, возвращает драйвер браузера
        """
        self.driver()
        s(by.xpath(x.username_field)).send_keys(self._login)
        s(by.xpath(x.password_field)).send_keys(self._password).press_enter()

    def book_entry(self):
        """
        Находит название книги на странице и заходит в нее
        """
        self.login()
        time.sleep(10)
        s(by.xpath(x.course)).click()
        return self._browser


if __name__ == '__main__':
    browser = Login('chrome', False, 'e2review1', 'Review1234', 'Medical-Surgical Nursing, Clinical').book_entry()
    time.sleep(60)
    browser.quit()
