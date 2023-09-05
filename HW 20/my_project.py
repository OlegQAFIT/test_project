# Создать минимум пять тестов для выбранного вами сайта
# Добавить документацию к тестом, чтобы можно было понять о чем тест
import re
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_1(driver):
    """
    From the drop-down list, try to select a silver subscription
    """
    driver.get('https://www.allsports.fit/by/')

    subscription_locator = '//div/header/div/ul/li[2]/a'
    driver.find_element(By.XPATH, subscription_locator).click()

    header_name_locator = "//main/section[1]/h1"
    wait = WebDriverWait(driver, 10)
    try:
        result_element = wait.until(EC.presence_of_element_located((By.XPATH, header_name_locator)))
        print(result_element.text)
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


def test_2(driver):
    """
    We check on the contact page, the correct phone number
    """
    driver.get('https://www.allsports.fit/by/')

    contacts_locator = '//div/ul/li[4]/a'
    driver.find_element(By.XPATH, contacts_locator).click()

    phone_locator = '//section[1]/p[16]'
    result_element = driver.find_element(By.XPATH, phone_locator)

    expected_phone_number = '+375 (44) 502-36-13'

    phone_pattern = r'\+\d{3} \(\d{2}\) \d{3}-\d{2}-\d{2}'
    actual_phone_number = re.search(phone_pattern, result_element.text).group()

    if expected_phone_number == actual_phone_number:
        print(f"Номер телефона совпадает: {actual_phone_number}")
    else:
        print(f"Номер телефона не совпадает. Ожидался: {expected_phone_number}, фактический: {actual_phone_number}")


def test_3(driver):
    """
    We check in the documentation tab that there is a document with the name -"Индивидуальные лицензии"
    """
    driver.get('https://www.allsports.fit/by/')

    doc_locator = '//div/footer/ul/li[8]/a'
    driver.find_element(By.XPATH, doc_locator).click()

    text_to_find = "Индивидуальные лицензии"
    elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{text_to_find}')]")

    if elements:
        print(f"Текст '{text_to_find}' найден на странице.")
    else:
        print(f"Текст '{text_to_find}' не найден на странице.")


def test_4(driver):
    """
    Checking the form for sending a message for an offer
    """
    driver.get('https://www.allsports.fit/by/')

    email_locator = '//main/section[1]/form/div/input'
    driver.find_element(By.XPATH, email_locator).send_keys('test123@gmail.com')

    get_locator = '//section[1]/form/button'
    driver.find_element(By.XPATH, get_locator).click()

    name_locator = '//section[7]/form/div[1]/input'
    phone_locator = '//section[7]/form/div[5]/input'
    city_locator = '//section[7]/form/div[2]/input'
    employe_locator = '//section[7]/form/div[4]/input'

    value_locator = '//main/section[7]/form/div[3]/button'
    driver.find_element(By.XPATH, value_locator).click()

    option_locator = '//section[7]/form/div[3]/div/button[1]'
    driver.find_element(By.XPATH, option_locator).click()

    driver.find_element(By.XPATH, name_locator).send_keys('ООО "Тест"')
    driver.find_element(By.XPATH, phone_locator).send_keys('375291112233')
    driver.find_element(By.XPATH, city_locator).send_keys('Минск')
    driver.find_element(By.XPATH, employe_locator).send_keys('Олег')

    get_2_locator = '//main/section[7]/form/button'
    driver.find_element(By.XPATH, get_2_locator).click()

    alert = Alert(driver)

    assert alert is not None
    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())
    alert.accept()


def test_5(driver):
    """
    Checking social media links
    """
    driver.get('https://www.allsports.fit/by/')

    instagram_locator = '//main/div/div/footer/div[2]/a[1]'
    linkedin_locator = '//main/div/div/footer/div[2]/a[2]'

    expected_instagram_url = 'https://www.instagram.com/allsports.fit/'
    expected_linkedin_url = 'https://www.linkedin.com/company/allsportsby'

    driver.find_element(By.XPATH, instagram_locator).click()

    driver.switch_to.window(driver.window_handles[1])

    actual_url = driver.current_url
    assert expected_instagram_url == actual_url, f"Expected Instagram URL: {expected_instagram_url}, Actual URL: {actual_url}"

    driver.close()

    driver.switch_to.window(driver.window_handles[0])

    driver.find_element(By.XPATH, linkedin_locator).click()

    driver.switch_to.window(driver.window_handles[1])

    actual_url = driver.current_url
    assert expected_linkedin_url == actual_url, f"Expected LinkedIn URL: {expected_linkedin_url}, Actual URL: {actual_url}"
