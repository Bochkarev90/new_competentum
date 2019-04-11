from selene.api import *
from selene.conditions import visible, exist
from input import variables as v
from input.excel import Excel
from pages.book_page import BookPage
from pages.usual_page import UsualPage
from subfunctions.subfunctions import compare_and_print


class TestChapter:

    """
    1.	TOC (Table of Contents) basket: expandable tree
        1.1.	Compare TOC listing against source document: all TOC entries should match exactly
        1.2.	Verify that TOC links open intended page/section
    """

    chapter_excel = Excel(v.path, v.chapter_number, v.set_number, v.lo_pos)
    book_page = BookPage(browser.driver(), chapter_excel.title())
    usual_page = UsualPage(browser.driver())

    def test_toc_modules_list(self, book_setup):
        print('\n\n Проверка списка модулей:')

        self.book_page.save_url()
        self.book_page.expand_modules_list()
        modules_on_book_page = self.book_page.text_pick_modules_list()

        n = 0
        for i in self.chapter_excel.modules():
            print('\n', i[0], modules_on_book_page[n], i[0] == modules_on_book_page[n], sep='\n')
            n += 1

    def test_correct_links(self):
        print('\n\n Проверка корректности ссылок из Assignment:')
        modules_on_book_page = self.book_page.text_pick_modules_list()
        for module_title in modules_on_book_page:
            self.book_page.module_title_click(module_title)

            s('h3').assure(visible, 30)

            module_title_h3 = self.usual_page.text_module_title_h3()
            compare_and_print(module_title, module_title_h3)

            s('iframe').should(exist, 15)
            self.usual_page.switch_to_frame()
            s('h1').assure(visible, 15)

            module_title_h1 = self.usual_page.text_module_title_h1()
            compare_and_print(module_title, module_title_h1)

            browser.open_url(self.book_page.url)

            s('span.title').assure(visible, 15)
            self.book_page.expand_modules_list()


if __name__ == '__main__':
    import pytest
    pytest.main()
