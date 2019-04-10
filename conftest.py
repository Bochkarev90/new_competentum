from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from input import variables as v
from input.excel import Excel
from selene.api import *
from selene.conditions import visible
import pytest
import time


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
    s(by.name('loginname')).send_keys(v.username)
    s(by.name('password')).send_keys(v.password).press_enter()
    s('.bookContainer').assure(visible, 30)
    yield
    s('button').click()


@pytest.yield_fixture(scope='module')
def book_setup(login_setup):
    my_bookshelf_url = browser.driver().current_url
    ss('.bookContainer').element_by(have.text(v.book)).click()
    chapter = Excel(v.path, v.chapter_number, v.set_number, v.lo_pos)
    yield chapter
    browser.open_url(my_bookshelf_url)
