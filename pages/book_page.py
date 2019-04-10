from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


class BookPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.book_title_h1_css = 'h1.titleHeader'
        self.book_title_p_css = 'p.bookTitle'

        self.contents_tab_css = 'button[role="tab"]:nth-child(1)'
        self.notebook_tab_css = 'button[role="tab"]:nth-child(2)'
        self.study_tools_tab_css = 'button[role="tab"]:nth-child(3)'

        self.image_css = 'img.withTitles'

        self.chapter_css = 'span.title'
        self.modules_css = 'ul[aria-hidden="false"]>li'

    def text_book_title_h1(self):
        return self.driver.find_element_by_css_selector(self.book_title_h1_css).text

    def text_book_title_p(self):
        return self.driver.find_element_by_css_selector(self.book_title_p_css).text

    def text_contents_tab(self):
        return self.driver.find_element_by_css_selector(self.contents_tab_css).text

    def text_notebook_tab(self):
        return self.driver.find_element_by_css_selector(self.notebook_tab_css).text

    def text_study_tools_tab(self):
        try:
            return self.driver.find_element_by_css_selector(self.study_tools_tab_css).text
        except NoSuchElementException:
            print("\n\nОтсутствуют Study Tools")

    def expand_modules_list(self):
        self.driver.find_element_by_css_selector(self.chapter_css).click()

    def text_pick_modules_list(self):
        modules_list = []
        for i in self.driver.find_elements_by_css_selector(self.modules_css):
            modules_list.append(i.text)
        return modules_list
