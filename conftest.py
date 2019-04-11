from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from input import variables as v
from input.excel import Excel
from selene.api import *
from selene.conditions import visible
import pytest
from pages.bookshelf_page import BookshelfPage
from pages.login_page import LoginPage


@pytest.yield_fixture(scope='module')
def browser_setup():
    # Если хром - добавляет английский язык браузеру
    if v.browser in ['c', 'chrome', 'Chrome']:
        chrome_options = Options()
        chrome_options.add_argument("--lang=en-us")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        browser.set_driver(driver)
    elif v.browser in ['f', 'firefox', 'Firefox']:
        pass
    else:
        print('Неверно указан браузер!')
    # Запускает платформу (revel или etext)
    browser.open_url('https://revel.pearson.com/#/start' if v.revel else 'http://etext.pearson.com/eplayer/login')
    yield
    browser.quit()


@pytest.yield_fixture(scope='module')
def login_setup(browser_setup):
    login_page = LoginPage(browser.driver())

    login_page.enter_username(v.username)
    login_page.enter_password(v.password)
    login_page.click_login()
    s('.bookContainer').assure(visible, 30)
    yield
    s('button').click()


@pytest.yield_fixture(scope='module')
def book_setup(login_setup):
    bookshelf_page = BookshelfPage(browser.driver(), v.book)
    bookshelf_page.chapter_entry()
    s('span.title').assure(visible, 30)
    yield
    browser.open_url(bookshelf_page.url)
