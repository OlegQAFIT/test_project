from helpers import BasePage


class FiveElement(BasePage):
    logo = '//img[@src="/resources/images/logo_.svg"]'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://5element.by/')

    def clk(self):
        self.hard_click(self.logo)

    def assert_main(self):
        self.wait_for_visible(self.logo)
        assert self.get_current_url() == 'https://5element.by/'
