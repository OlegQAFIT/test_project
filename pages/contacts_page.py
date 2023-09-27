from helpers.base import BasePage


class ContactsPage(BasePage):
    contacts_locator = '//div/ul/li[4]/a'
    act_result = '//div/div/main/section[1]/p[7]/a'
    expected_result = '+375 (44) 502-36-13'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.allsports.fit/by/')

    def clc(self):
        self.hard_click(self.contacts_locator)

    def assert_phone(self):
        self.assert_text_in_element(self.act_result, self.expected_result)
