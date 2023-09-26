# 2 Написать методы для работы с
# Сайт где можно взять элемент
# В отдельный файл запихнул методы для наглядности и плюс файл в base

from telnetlib import EC
from tkinter.tix import Select
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def check_checkbox(driver, locator):
    element = driver.find_element(By.XPATH, locator)
    element.click()


def uncheck_checkbox(driver, locator):
    element = driver.find_element(By.XPATH, locator)
    if element.is_selected():
        element.click()
    else:
        print("The element is already selected")


def scroll_down(driver):
    driver.execute_script("window.scrollTo(0, window.innerHeight);")


def select_radio_button(driver, locator):
    element = driver.find_element(By.XPATH, locator)
    element.click()


def dropdown_select(driver, locator, value):
    element = Select(driver.find_element(By.XPATH, locator))
    element.select_by_value(value)


def get_input_text(driver, locator, text):
    element = driver.find_element(By.XPATH, locator)
    element.clear()
    element.send_keys(text)
    element.get_attribute(text)


def get_attribute(driver, locator, attribute_name):
    element = driver.find_element(By.XPATH, locator)
    element.get_attribute(attribute_name)


def wait_for_element_is_displayed(driver, locator):
    try:
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
    except WebDriverException:
        assert False, f"Element {locator} is not displayed"


def wait_for_element_is_enabled(driver, locator):
    try:
        return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator)))
    except WebDriverException:
        assert False, f"Element {locator} is not enabled"