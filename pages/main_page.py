import time

from helpers.base import BasePage


# class MainPage(BasePage, FooterElement, HeaderElement):
class MainPage(BasePage):
    level = '//form/div[2]/div[3]/div/label[2]/div'
    type_subscription_locator = '//form/div[2]/div[3]/button'
    email_locator = '//main/section[1]/form/div/input'
    get_locator = '//section[1]/form/button'
    name_locator = '//section[7]/form/div[1]/input'
    phone_locator = '//section[7]/form/div[5]/input'
    city_locator = '//section[7]/form/div[2]/input'
    employe_locator = '//section[7]/form/div[4]/input'
    value_locator = '//form/div[3]/button'
    option_locator = '//section[7]/form/div[3]/div/button[1]'
    get_2_locator = '//main/section[7]/form/button'

    def __init__(self, driver):
        self.text_employe = 'Олег'
        self.text_city = 'Минск'
        self.text_phone = '375 29 111 22 33'
        self.text_name = 'ОАО Проверка'
        self.text_email = 'test@gmail.com'
        self.driver = driver

    def open(self):
        self.driver.get('https://www.allsports.fit/by/')

    def clc(self):
        self.hard_click(self.type_subscription_locator)

    def assert_main(self):
        self.wait_for_visible(self.level)

    def enter_email(self):
        self.fill(self.email_locator, self.text_email)

    def clc_get_1(self):
        self.hard_click(self.get_locator)

    def drop_clc(self):
        self.hard_click(self.value_locator)
        self.hard_click(self.option_locator)

    def fill_form(self, email_locator, name_locator, phone_locator, city_locator, employe_locator):
        self.fill(email_locator, self.text_email)
        self.fill(name_locator, self.text_name)
        self.fill(phone_locator, self.text_phone)
        self.fill(city_locator, self.text_city)
        self.fill(employe_locator, self.text_employe)

    def clc_get_2(self):
        self.hard_click(self.get_2_locator)

    def assert_form(self):
        time.sleep(2)
        self.handle_alert("Спасибо! Мы скоро свяжемся с вами!")
