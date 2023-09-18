from pages.login_page import LoginPage
import allure

@allure.suite("Test login forms")
class TestLogin:
    @allure.description("test valid email")
    def test_valid_email(self,driver):
        login_page = LoginPage(driver,'https://www.ukazka.ru/login.php')
        login_page.open()
        login_page.fill_fields_and_submit()

    @allure.description("test invalid email")
    def test_invalid_email(self, driver):
        login_page = LoginPage(driver, 'https://www.ukazka.ru/login.php')
        login_page.open()
        login_page.fill_fields_and_submit_with_error()

    @allure.description("test error message")
    def test_error(self, driver, error_text="Неправильно указан Е-Мейл или пароль!"):
        login_page = LoginPage(driver, 'https://www.ukazka.ru/login.php')
        login_page.open()
        login_page.show_error()
        assert error_text == error_text



            







