from helpers.base import BasePage
from helpers.fields import FieldsWebElement


class ObjectPage(BasePage):
    delete = FieldsWebElement('xpath') # Вставить правильный локатор вместо xpath

    def open(self):
        self.driver.get('https://5element.by/')

    def assert_that_delete_icon_is_visible(self):
        self.delete.wait_for_visible()


        self.wait_for_visible(self.delete_locator)