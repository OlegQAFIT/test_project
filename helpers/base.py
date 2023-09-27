from tkinter.tix import Select
from selenium.common import WebDriverException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __int__(self, driver):
        self.driver = driver
        self.WAIT_UNTIL = 5

    def fill(self, locator, text):                              #Этот код используется для заполнения поля на веб-странице
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def clear(self, locator):                                   #Метод cиспользуется для очистки текстового поля, представленного элементом
        element = self.wait_for_visible(locator)
        element.clear()

    def wait_for_visible(self, locator):                        #Метод используется для ожидания появления элемента на странице
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, locator)))
        except WebDriverException:
            assert False, f"Element {locator} not clicable"

    def find_element_text(self, locator):                      #Метод используется для поиска элемента на веб-странице с помощью заданного локатора
        element = self.driver.find_element(By.XPATH, locator)
        return element.text

    def add_cookie(self, name, value):                        #Метод используется для добавления куки (cookie) к текущей сессии браузера с заданным именем (name) и значением (value).
        self.driver.add_cookie({'name': name, 'value': value})
        self.driver.refresh()

    def delete_cookies(self):
        self.driver.delete_cookies()
        self.driver.refresh()

    def check_checkbox(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()

    def uncheck_checkbox(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        if element.is_selected():
            element.click()
        else:
            print("The element is already selected")

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, window.innerHeight);")

    def click_on(self, locator):
        element = self.wait_for_visible(locator)
        element.click()

    def switch_to_main_window(self):
        self.driver.switch_to.window(self.main_window_handle)

    def select_radio_button(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()

    def dropdown_select(self, locator, value):
        element = Select(self.driver.find_element(By.XPATH, locator))
        element.select_by_value(value)

    def handle_alert(self, expected_text=None):
        alert = Alert(self.driver)
        if expected_text:
            assert alert.text == expected_text
        alert.accept()

    def get_input_text(self, locator, text):
        element = self.driver.find_element(By.XPATH, locator)
        element.clear()
        element.send_keys(text)
        element.get_attribute(text)

    def get_attribute(self, locator, attribute_name):
        element = self.driver.find_element(By.XPATH, locator)
        element.get_attribute(attribute_name)

    def wait_for_element_is_displayed(self, locator):
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        except WebDriverException:
            assert False, f"Element {locator} is not displayed"

    def wait_for_element_is_enabled(self, locator):
        try:
            return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator)))
        except WebDriverException:
            assert False, f"Element {locator} is not enabled"

    def hard_click(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].click();", element)

    def get_current_url(self):
        return self.driver.current_url

    def clear(self, locator):
        element = self.wait_for_visible(locator)
        element.clear()

    def select_by_value(self, select, value):
        element = self.wait_for_visible(select)
        select = Select(element)
        select.select_by_value(value)

    def switch_to_iframe(self):
        self.driver.switch_to.frame(self.wait_for_visible('//iframe'))

    def set_display_none(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script('arguments[0].setAttribute("display", arguments[1])', element, 'none')

    def prompt_alert(self):
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.send_keys("Answer")
        alert.accept()

    def open_new_window(self):
        self.driver.execute_script("window.open()")
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        self.driver.close()

    def assert_text_in_element(self, locator, expected_result):
        element = self.driver.find_element(By.XPATH, locator)
        assert expected_result == element.text, "Text not the same"

    def assert_value_in_element_attribute(self, locator, attribute, expected_result):
        element = self.driver.find_element(By.XPATH, locator)
        value = element.get_attribute(attribute)
        assert value == expected_result, "Attribute value not the same"

    def assert_actual_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Expected URL:{expected_url}, Actual URL: {actual_url}"
