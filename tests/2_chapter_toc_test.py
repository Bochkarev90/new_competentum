# from selene.conditions import visible
# from selene.api import *
# from input import variables as v
# import time
# # from pages.book_page import BookPage
#
#
# class TestChapter:
#
#     """
#     1.	TOC (Table of Contents) basket: expandable tree
#         1.1.	Compare TOC listing against source document: all TOC entries should match exactly
#         1.2.	Verify that TOC links open intended page/section
#     """
#
#     chapter_excel = None
#     modules_on_book_page = []
#     # url = browser.driver().current_url
#     # book_page = BookPage(browser)
#
#     def test_toc__modules_list(self, book_setup):
#         print('\n\n Проверка списка модулей:')
#
#         self.chapter_excel = book_setup
#         # self.book_page.chapter_click(self.chapter_excel.title())
#         ss('span.title').element_by(have.text(self.chapter_excel.title())).click()
#
#         for i in ss('ul[aria-hidden="false"]>li'):
#             self.modules_on_book_page.append(i.text)
#
#         n = 0
#         for i in self.chapter_excel.modules():
#             print('\n', i[0], self.modules_on_book_page[n], i[0] == self.modules_on_book_page[n], sep='\n')
#             n += 1
#
#     def test_correct_links(self):
#         print('\n\n Проверка корректности ссылок из Assignment:')
#         url = browser.driver().current_url
#         for i in self.modules_on_book_page:
#             s(by.xpath('//span[contains(text(), "' + i + '")]')).assure(visible, 20).click()
#             time.sleep(10)
#             s('iframe')
#             browser.driver().switch_to.frame('contentIframe')
#             s('h1').assure(visible, 20)
#             print('\n\n' + s('h1').text)
#             browser.open_url(url)
#             time.sleep(10)
#             ss('span.title').element_by(have.text(self.chapter_excel.title())).click()
#
#
# if __name__ == '__main__':
#     import pytest
#     pytest.main()
