from conftest import driver
from helpers.base import BasePage
from elements import FooterElement, HeaderElement


class MainPage(BasePage, FooterElement, HeaderElement):
    def open(self):
        self.driver.get('https://5element.by/')

    def open(self):
        self.driver.get('https://5element.by/')
        main_page_19 = MainPage(driver)
        main_page_19.click_on_object_item()
