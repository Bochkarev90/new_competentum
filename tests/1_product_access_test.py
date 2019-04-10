from selene.conditions import visible
from selene.api import *
from input import variables as v
from pages.book_page import BookPage


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
#     def test_book_info_window(self, login_setup):
#         global book
#         book = ss('.bookContainer').element_by(have.text(v.book))  # Book at the "My Bookshelf Page"
#         book.s(by.be_following_sibling()).click()  # About link
#
#         if s('p.body').text != v.book:
#             print("Название курса не соответствует в теле окна информации о книге")
#             print(s('p.body').text, v.book, sep='\n')
#
#         if s('div.desc-container').text != v.book:
#             print("Название курса не соответствует в описании в окне информации о книге")
#             print(s('div.desc-container').text, v.book, sep='\n')
#
#         # TODO: проверить загрузку картинки
#
#         s('.closeDialog').click()
#
#     def test_book_entry(self):
#         book.click()
#         s('h1').assure(visible, 30)
#         book_page = BookPage()
#
#         if s('h1').text != v.book:
#             print("\n\nНазвание курса не соответствует в h1")
#             print(s('h1').text, v.book, sep='\n')
#
#         if s('p.bookTitle').text != v.book:
#             print("\n\nНазвание курса не соответствует в абзаце")
#             print(s('p.bookTitle').text, v.book, sep='\n')
#
#         # TODO: проверить загрузку картинки
#
#         if s(book_page.contentsTab_button).text != 'Contents':
#             print("\n\nВкладка Contents???")
#             print(s(book_page.contentsTab_button).text)
#
#         if s(book_page.notebookTab_button).text != 'Notebook':
#             print("\n\nВкладка Notebook???")
#             print(s(book_page.notebookTab_button).text)
#
#         if s(book_page.studyToolsTab_button).text != 'Study Tools':
#             print("\n\nВкладка Study Tools???")
#             print(s(book_page.studyToolsTab_button).text) \
#                 if s(book_page.studyToolsTab_button).text else "Нет вкладки Study Tools"
#
#         browser.driver().back()


if __name__ == '__main__':
    import pytest
    pytest.main()
