from helpers import BasePage


class SubmitForm(BasePage):
    first_name_locator = '//form/table/tbody/tr[2]/td[2]/input'
    last_name_locator = '//form/table/tbody/tr[3]/td[2]/input'
    phone_locator = '//form/table/tbody/tr[4]/td[2]/input'
    email_locator = '//*[@id="userName"]'
    address_locator = '//form/table/tbody/tr[7]/td[2]/input'
    city_locator = '//form/table/tbody/tr[8]/td[2]/input'
    state_province_locator = '//form/table/tbody/tr[9]/td[2]/input'
    postal_code_locator = '//form/table/tbody/tr[10]/td[2]/input'
    user_name_locator = '//*[@id="email"]'
    password_locator = '//form/table/tbody/tr[14]/td[2]/input'
    confirm_password_locator = '//form/table/tbody/tr[15]/td[2]/input'
    send_locator = '//form/table/tbody/tr[17]/td/input'
    file = "Dear Oleg Atrokhau"
    file_2 = "Note: Your user name is Olegfit"

    def __init__(self, driver):
        self.text_first_name = 'Oleg'
        self.text_last_name = 'Atrokhau'
        self.text_phone = '375291112233'
        self.text_email = 'test123@gmail.com'
        self.text_address = 'Internationalnaia 36'
        self.text_city = 'Minsk'
        self.text_state_province = 'Minsk Region'
        self.text_postal_code = '220033'
        self.text_user_name = 'Olegfit'
        self.text_password = 'qwerty1234'
        self.text_confirm_password = 'qwerty1234'
        self.driver = driver

    def open(self):
        self.driver.get('http://demo.guru99.com/test/newtours/register.php')

    def enter_first_name(self):
        self.fill(self.first_name_locator, self.text_first_name)

    def enter_last_name(self):
        self.fill(self.last_name_locator, self.text_last_name)

    def enter_phone(self):
        self.fill(self.phone_locator, self.text_phone)

    def enter_email(self):
        self.fill(self.email_locator, self.text_email)

    def enter_address(self):
        self.fill(self.address_locator, self.text_address)

    def enter_city(self):
        self.fill(self.city_locator, self.text_city)

    def enter_state_province(self):
        self.fill(self.state_province_locator, self.text_state_province)

    def enter_postal_code(self):
        self.fill(self.postal_code_locator, self.text_postal_code)

    def enter_user_name(self):
        self.fill(self.user_name_locator, self.text_user_name)

    def enter_password(self):
        self.fill(self.password_locator, self.text_password)

    def enter_confirm_password(self):
        self.fill(self.confirm_password_locator, self.text_confirm_password)

    def clk(self):
        self.hard_click(self.send_locator)

    def assert_reg(self, file):
        if file in self.driver.page_source:
            print(f"Текст '{file}' найден на странице.")
        else:
            print(f"Текст '{file}' не найден на странице.")
