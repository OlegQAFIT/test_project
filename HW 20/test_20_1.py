# Задание 1:
# 1. Открыйть сайт http://thedemosite.co.uk/login.php
# 2. Ввести имя в поле username
# 3. Ввести пароль в поле password
# 4. Нажать на кнопку Test Login
# 5. Проверить, что Successful Login отображаются
from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_1(driver):
    driver.get('http://thedemosite.co.uk/login.php')

    username_locator = '[name="username"]'
    password_locator = '[type="password"]'

    driver.find_element(By.CSS_SELECTOR, username_locator).send_keys('Oleg')
    driver.find_element(By.CSS_SELECTOR, password_locator).send_keys('qwerty1234')

    login_locator = '//table/tbody/tr[3]/td[2]/p/input'

    driver.find_element(By.XPATH, login_locator).click()

    success_message_locator = "//b[contains(text(), 'Successful Login')]"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, success_message_locator)))
    success_message = driver.find_element(By.XPATH, success_message_locator).text
    assert "Successful Login" in success_message, "Successful Login Error"
