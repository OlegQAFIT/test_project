from helpers import BasePage


class LoginForm(BasePage):
    username_locator = '//table/tbody/tr[1]/td[2]/p/input'
    password_locator = '//tbody/tr[2]/td[2]/p/input'
    login_locator = '//table/tbody/tr[3]/td[2]/p/input'

    def __init__(self, driver):
        self.text_username = 'Олег'
        self.text_password = 'qwerty1234'
        self.driver = driver

    def open(self):
        self.driver.get('http://thedemosite.co.uk/login.php')

    def enter_username(self):
        self.fill(self.username_locator, self.text_username)

    def enter_password(self):
        self.fill(self.password_locator, self.text_password)

    def clk(self):
        self.hard_click(self.login_locator)
