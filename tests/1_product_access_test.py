# from selene.api import *
# from selene.conditions import visible
# from input import variables as v
# from pages.book_page import BookPage
# from pages.bookshelf_page import BookshelfPage
# from subfunctions.subfunctions import compare_and_print
#
#
# class TestProductAccess:
#
#     """
#     1.	Go to the URL provided by the Producer (https://etext.pearson.com/eplayer/login) or open the eText
#         app (depending which testing configuration is being used).
#     2.	Log in using the account provided in testing request.  The “My Bookshelf” page will be displayed once logged in.
#     3.	At the “My Bookshelf” page, locate the appropriate title
#     4.	Click the   or about  link (in app)
#     4.1.	Verify the course information matches the information provided in the testing request
#             and supporting documentation.
#     5.	Enter the course. Cover page should load. There will be three tabs, in order as follows:
#         Contents, Notebook and Study tools.
#     6.	If the default font is too large, log it as an issue. The font should be medium sized.
#     """
#
#     bookshelf_page = BookshelfPage(browser.driver(), v.book)
#     book_page = BookPage(browser.driver(), '')
#
#     def test_book_info_window(self, login_setup):
#
#         self.bookshelf_page.open_info_window()
#
#         title_p = self.bookshelf_page.info_window_book_title_p()
#         title_div = self.bookshelf_page.info_window_book_title_div()
#
#         if title_p != v.book:
#             print("\nОтличается название курса в окне информации о книге в <p>")
#             compare_and_print(title_p, v.book)
#
#         if title_div != v.book:
#             print("\nОтличается название курса в окне информации о книге в <div>")
#             compare_and_print(title_div, v.book)
#
#         # TODO: проверить загрузку картинки
#
#         self.bookshelf_page.close_info_window()
#
#     def test_book_entry(self):
#
#         self.bookshelf_page.chapter_entry()
#
#         s('p.bookTitle').assure(visible, 30)
#
#         book_title_h1 = self.book_page.text_book_title_h1()
#         book_title_p = self.book_page.text_book_title_p()
#
#         if book_title_h1 != v.book:
#             print("\nОтличается название курса на странице книги в <h1>")
#             compare_and_print(book_title_h1, v.book)
#
#         if book_title_p != v.book:
#             print("\nОтличается название курса на странице книги в <p>")
#             compare_and_print(book_title_p, v.book)
#
#         # TODO: проверить загрузку картинки
#
#         if self.book_page.text_contents_tab() != 'Contents':
#             print("\nВкладка Contents???")
#             print(self.book_page.text_contents_tab()) \
#                 if self.book_page.text_contents_tab() else "Отсутствует вкладка Contents"
#
#         if self.book_page.text_notebook_tab() != 'Notebook':
#             print("\nВкладка Notebook???")
#             print(self.book_page.text_notebook_tab()) \
#                 if self.book_page.text_notebook_tab() else "Отсутствует вкладка Notebook"
#
#         if self.book_page.text_study_tools_tab() != 'Study Tools':
#             print("\nВкладка Study Tools???")
#             print(self.book_page.text_study_tools_tab()) \
#                 if self.book_page.text_study_tools_tab() else "Отсутствуют Study Tools"
#
#         browser.driver().back()
#
#
# if __name__ == '__main__':
#     import pytest
#     pytest.main()
