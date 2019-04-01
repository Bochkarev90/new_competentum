from input.excel import Excel
from input import variables as v
from tests.login import Login
import time

chapter_info = Excel(v.path, v.chapter_number, v.set_number).chapter_info()
browser = Login(v.browser, v.revel, v.username, v.password).login()
time.sleep(10)

if v.browser == 'chrome':
    browser.quit()
