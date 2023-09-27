from helpers import BasePage


class HeaderElement(BasePage):
    object_locator = '//li[1]/a'

    def click_on_object_item(self):
        self.click_on(self.object_locator)
