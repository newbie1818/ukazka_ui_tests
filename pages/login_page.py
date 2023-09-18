from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators as Locators

class LoginPage(BasePage):

    def fill_fields_and_submit(self):
        email = "jane123@getairmail.com"
        password = "1!Apple7&"
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.BUTTON).click()


    def fill_fields_and_submit_with_error(self):
        email = "jane@getairmail.com"
        password = "1!Apple7&"
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.BUTTON).click()

    def show_error(self):
        email = "jane@getairmail.com"
        password = "1!Apple7&"
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.BUTTON).click()
        self.element_is_visible(Locators.ERROR).text








