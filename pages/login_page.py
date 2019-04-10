from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.username_input_name = 'loginname'
        self.password_input_name = 'password'
        self.login_button_css = 'button.form_button'

    def enter_username(self, username):
        self.driver.find_element_by_name(self.username_input_name).clear()
        self.driver.find_element_by_name(self.username_input_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_input_name).clear()
        self.driver.find_element_by_name(self.password_input_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_css_selector(self.login_button_css).click()
