import allure

from helpers import BasePage


class HW25(BasePage):
    list_alert_locator = '//*[@id="content"]/ul/li[29]/a'
    alert_locator = '//*[@id="content"]/div/ul/li[1]/button'
    confirm_alert_locator = '//*[@id="content"]/div/ul/li[1]/button'
    prompt_alert_locator = '//*[@id="content"]/div/ul/li[3]/button'
    frame_locator = '//*[@id="content"]/ul/li[22]/a'
    iframe_locator = '//*[@id="content"]/div/ul/li[2]/a'
    text = '//iframe[@id="mce_0_ifr"]'
    download_buttom_locator = '//*[@id="content"]/ul/li[17]/a'
    download_click_locator = 'https://the-internet.herokuapp.com/download/2.jpg'
    download_destination = 'D:/'
    upload_buttom_locator = '//*[@id="content"]/ul/li[18]/a'
    file_click_locator = '//input[@type="file"]'
    file_to_upload = 'C:/Users/test/Desktop/by_employees_template (8).xlsx'

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Open page "the-internet.herokuapp.com"')
    def open(self):
        self.driver.get('https://the-internet.herokuapp.com/')

    @allure.step('Click on the button to open the list with Alert')
    def clk(self):
        self.hard_click(self.list_alert_locator)

    @allure.step('Click to play simple alert')
    def clk_simple_alert(self):
        self.hard_click(self.alert_locator)

    @allure.step('Click to play confirm alert')
    def clk_confirm_alert(self):
        self.hard_click(self.confirm_alert_locator)

    @allure.step('Click to play promt alert')
    def clk_promt_alert(self):
        self.hard_click(self.prompt_alert_locator)

    @allure.step('Click on OK in the alert')
    def use_simple_alert(self):
        self.alert_ok()

    @allure.step('Click on OK in the alert')
    def use_confirm_alert(self):
        self.alert_ok()

    @allure.step('Click on OK in the alert')
    def use_prompt_alert(self):
        self.prompt_alert()

    @allure.step('Click on dissmis in the alert')
    def use_dissmis(self):
        self.alert_dismiss()

    @allure.step('Switching to iframe')
    def assert_search_iframe(self):
        self.switch_to_iframe()

    @allure.step('Click on the iframe tab')
    def clk_frame(self):
        self.hard_click(self.frame_locator)

    @allure.step('Click on iframe')
    def clk_iframe(self):
        self.hard_click(self.iframe_locator)

    @allure.step('Checking that there is text')
    def check_text(self):
        self.assert_text_in_element('//iframe[@id="mce_0_ifr"]', "Your content goes here.")

    @allure.step('Click to go to the download tab')
    def clk_download(self):
        self.hard_click(self.download_buttom_locator)

    @allure.step('We are trying to download the file and check that it has been downloaded')
    def assert_dow(self):
        self.download_file(self.download_click_locator, self.download_destination)

    @allure.step('Click to go to the upload tab')
    def clk_upload(self):
        self.hard_click(self.upload_buttom_locator)

    @allure.step('We are trying to download a file and check that it is uploaded')
    def assert_upl(self):
        self.upload_file(self.file_click_locator, self.file_to_upload)
