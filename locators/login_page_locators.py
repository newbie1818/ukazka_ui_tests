from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL = (By.ID,'pole_login')
    PASSWORD = (By.NAME,'parol')
    BUTTON = (By.NAME, 'knopka')
    ERROR = (By.CLASS_NAME, 'r')




