from pages.base_page import BasePage


class BookshelfPage(BasePage):

    def __init__(self, driver, book_title):
        super().__init__(driver)

        self.logout_button_css = 'button[label="Log Out"]'

        self.book_container_button_xpath = '//span[contains(text(), "' + book_title + '")]/parent::button'
        self.info_window_icon_xpath = self.book_container_button_xpath + '/following-sibling::button'

        self.info_window_p_css = 'p.body'
        self.info_window_div_css = 'div.desc-container'
        self.close_info_window_button_css = 'button.closeDialog'

    def open_info_window(self):
        self.driver.find_element_by_xpath(self.info_window_icon_xpath).click()

    def info_window_book_title_p(self):
        return self.driver.find_element_by_css_selector(self.info_window_p_css).text

    def info_window_book_title_div(self):
        return self.driver.find_element_by_css_selector(self.info_window_div_css).text

    def close_info_window(self):
        self.driver.find_element_by_css_selector(self.close_info_window_button_css).click()

    def chapter_entry(self):
        self.driver.find_element_by_xpath(self.book_container_button_xpath).click()

    def logout(self):
        self.driver.find_element_by_css(self.logout_button_css).click()
