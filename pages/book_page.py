from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


class BookPage(BasePage):

    def __init__(self, driver, chapter_title):
        super().__init__(driver)

        self.book_title_h1_css = 'h1.titleHeader'
        self.book_title_p_css = 'p.bookTitle'

        self.contents_tab_css = 'button[role="tab"]:nth-child(1)'
        self.notebook_tab_css = 'button[role="tab"]:nth-child(2)'
        self.study_tools_tab_css = 'button[role="tab"]:nth-child(3)'

        self.image_css = 'img.withTitles'

        self.chapter_span_xpath = '//span[contains(text(), "' + chapter_title + '")]'
        self.modules_li_css = 'ul[aria-hidden="false"]>li'
        self.module_span_xpath_start = '//span[contains(text(), "'
        self.module_span_xpath_end = '")]'

    def text_book_title_h1(self):
        return self.driver.find_element_by_css_selector(self.book_title_h1_css).text

    def text_book_title_p(self):
        return self.driver.find_element_by_css_selector(self.book_title_p_css).text

    def text_contents_tab(self):
        try:
            return self.driver.find_element_by_css_selector(self.contents_tab_css).text
        except NoSuchElementException:
            return False

    def text_notebook_tab(self):
        try:
            return self.driver.find_element_by_css_selector(self.notebook_tab_css).text
        except NoSuchElementException:
            return False

    def text_study_tools_tab(self):
        try:
            return self.driver.find_element_by_css_selector(self.study_tools_tab_css).text
        except NoSuchElementException:
            return False

    def expand_modules_list(self):
        self.driver.find_element_by_xpath(self.chapter_span_xpath).click()

    def text_pick_modules_list(self):
        modules_list = []
        for i in self.driver.find_elements_by_css_selector(self.modules_li_css):
            modules_list.append(i.text)
        return modules_list

    def module_title_click(self, module_title):
        self.driver.find_element_by_xpath(
            self.module_span_xpath_start + module_title + self.module_span_xpath_end
        ).click()
