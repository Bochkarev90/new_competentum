from selene.conditions import visible
from selene.api import *
from input import variables as v
import time

#
# class TestBookInfo:
#
#     def test_book_info_window(self, login_setup):
#         global book
#         book = ss('.bookContainer').element_by(have.text(v.book))
#         book.s(by.be_following_sibling()).click()
#         assert s('p.body').text == v.book
#         # assert s('div.desc-container').text == v.book
#         s('.closeDialog').click()
#
#     def test_book_entry(self):
#         time.sleep(2)
#         book.click()
#         s('h1').assure(visible, 30).assure(have.text(v.book))
#         assert s('h1').text == v.book
#         browser.driver().back()


if __name__ == '__main__':
    import pytest
    pytest.main()
