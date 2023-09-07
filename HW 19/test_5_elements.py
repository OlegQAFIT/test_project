from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

logo = '//div[1]/div[2]/div/div[1]/div[1]/div[1]/a/img'  # selector


class Test5Element:

    def test_page(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get('https://5element.by/')

        locator_logo = driver.find_element(By.XPATH, logo)

        driver.save_screenshot('open_5th_element_page.png')
        assert WebDriverWait(driver, 5).until(EC.visibility_of(locator_logo))
