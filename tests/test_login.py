from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.api import *
import pytest
from input import variables as v


class TestLogin:
    @pytest.fixture()
    def test_setup(self):
        global driver
        # Если хром - добавляет английский язык браузеру
        # if v.browser == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument("--lang=en-us")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        # driver.implicitly_wait(10)
        # browser.set_driver(driver)
        # Запускает тот браузер, который указан в variables
        # config.browser_name = v.browser
        # Запускает платформу (revel или etext)
        # browser.open_url('https://revel.pearson.com/#/start' if v.revel else 'http://etext.pearson.com/eplayer/login')
        driver.get('https://revel.pearson.com/#/start' if v.revel else 'http://etext.pearson.com/eplayer/login')
        yield
        driver.close()
        driver.quit()
        print("Ура!!!")

    def test_login(self, test_setup):
        driver.find_element_by_name('loginname').send_keys(v.username)
        driver.find_element_by_name('password').send_keys(v.password)
        driver.find_element_by_css_selector('.form_button').click()
    #
    # def book_entry(self):
    #     """
    #     Находит название книги на странице и заходит в нее
    #     """
    #     self.login()
    #     time.sleep(10)
    #     s(by.xpath(x.course)).click()
    #     return self._browser


if __name__ == '__main__':
    pass
