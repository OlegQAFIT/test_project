from helpers.base import BasePage


class FooterElement(BasePage):
    instagram_locator = '//main/div/div/footer/div[2]/a[1]'
    linkedin_locator = '//main/div/div/footer/div[2]/a[2]'
    user_agreements_locator = '//div/footer/ul/li[8]/a'
    file = "Индивидуальные лицензии"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.allsports.fit/by/')

    def click_on_instagram(self):
        self.click_on(self.instagram_locator)

    def click_on_docs(self):
        self.click_on(self.user_agreements_locator)

    def click_on_linkedin(self):
        self.click_on(self.linkedin_locator)

    def assert_dok(self, file):
        if file in self.driver.page_source:
            print(f"Текст '{file}' найден на странице.")
        else:
            print(f"Текст '{file}' не найден на странице.")

    def assert_instagram(self):
        self.wait_for_visible(self.instagram_locator)
        assert self.get_current_url() == 'https://www.instagram.com/allsports.fit/'

    def assert_linkedin(self):
        self.wait_for_visible(self.linkedin_locator)
        assert self.get_current_url() == 'https://www.linkedin.com/company/allsportsby'
