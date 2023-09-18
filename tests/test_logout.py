from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
import allure

@allure.suite("Test logout function")
class TestLogout:
        @allure.description("test logout")
        def test_logout(auth):
                logout = MainPage()
                logout.open()
                logout.quit_the_account()

        element = WebDriverWait(driver=webdriver,timeout=10).until(
            EC.presence_of_element_located ((By.CLASS_NAME, 'r'))
        )
        print(element)
        assert element == "Вы завершили сеанс работы с системой заказов!"