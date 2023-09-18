import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def auth( ):
    email = 'jane123@getairmail.com'
    password = '1!Apple7&'
    driver = webdriver.Chrome().get('https://www.ukazka.ru/login.php')
    driver.find_element(By.ID, 'pole_login').send_keys(email)
    driver.find_element(By.NAME, 'parol').send_keys(password)
    driver.find_element(By.NAME, 'knopka').click()
    yield auth
    print("Логин прошел успешно")
    driver.get('https://www.ukazka.ru/kabinet')








