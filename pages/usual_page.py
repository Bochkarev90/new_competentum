from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage


class UsualPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.module_title_h3_css = 'h3.headerTitle '
        self.frame_iframe_css = 'iframe#contentIframe'
        self.module_title_h1_css = 'h1.title'

    def text_module_title_h3(self):
        return self.driver.find_element_by_css_selector(self.module_title_h3_css).text

    def switch_to_frame(self):
        try:
            self.driver.switch_to.frame(self.driver.find_element_by_css_selector(self.frame_iframe_css))
        except NoSuchElementException:
            return

    def text_module_title_h1(self):
        return self.driver.find_element_by_css_selector(self.module_title_h1_css).text
