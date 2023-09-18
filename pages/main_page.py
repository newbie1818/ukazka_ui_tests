
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Locators
from selenium import webdriver

class MainPage(BasePage):

    def quit_the_account(driver, url='https://www.ukazka.ru/kabinet'):
        self.element_is_visible(Locators.LOGOUT).click()