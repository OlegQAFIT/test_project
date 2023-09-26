# Задание 2
# 1. Открыть сайт http://demo.guru99.com/test/newtours/register.php
# 2. Заполнить все поля
# 3. Нажать кнопку Submit
# 4. Проверить, что отображается правильно имя и фамилия
# Подсказка xpath ".//tr//table//font[3]”
# 5.Проверить, что отображается правильно username
# Подсказка xpath ".//tr//table//font[5]”
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_2(driver):
    driver.get('http://demo.guru99.com/test/newtours/register.php')

    first_name_locator = '[name="firstName"]'
    last_name_locator = '[name="lastName"]'
    phone_locator = '[name="phone"]'
    email_locator = '[name="email"]'
    address_locator = '[name="address1"]'
    city_locator = '[name="city"]'
    state_province_locator = '[name="state"]'
    postal_code_locator = '[name="postalCode"]'
    country_select_locator = '[name="country"]'
    user_name_locator = '[name="email"]'
    password_locator = '[name="password"]'
    confirm_password_locator = '[name="confirmPassword"]'

    driver.find_element(By.CSS_SELECTOR, first_name_locator).send_keys('Oleg')
    driver.find_element(By.CSS_SELECTOR, last_name_locator).send_keys('Atrokhau')
    driver.find_element(By.CSS_SELECTOR, phone_locator).send_keys('375291112233')
    driver.find_element(By.CSS_SELECTOR, email_locator).send_keys('test123@gmail.com')
    driver.find_element(By.CSS_SELECTOR, address_locator).send_keys('Internationalnaia 36')
    driver.find_element(By.CSS_SELECTOR, city_locator).send_keys('Minsk')
    driver.find_element(By.CSS_SELECTOR, state_province_locator).send_keys('Minsk Region')
    driver.find_element(By.CSS_SELECTOR, postal_code_locator).send_keys('220033')

    country_select = Select(driver.find_element(By.NAME, 'country'))
    country_select.select_by_value('BELARUS')

    driver.find_element(By.CSS_SELECTOR, user_name_locator).send_keys('Olegfit')
    driver.find_element(By.CSS_SELECTOR, password_locator).send_keys('qwerty1234')
    driver.find_element(By.CSS_SELECTOR, confirm_password_locator).send_keys('qwerty1234')

    send_locator = '[name="submit"]'
    driver.find_element(By.CSS_SELECTOR, send_locator).click()

    first_last_name_locator = "//tbody/tr[3]/td/p[1]/font/b"
    result_element = driver.find_element(By.XPATH, first_last_name_locator)
    print(result_element.text)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, first_last_name_locator)))

    username_locator = "//tbody/tr[3]/td/p[3]/font/b"
    result_element = driver.find_element(By.XPATH, username_locator)
    print(result_element.text)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, username_locator)))
