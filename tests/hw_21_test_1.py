# 1 Написать тест на проверку следующих элементов на сайте bbc.com с помощью css и xpath
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import url_to_be
from selenium.webdriver.support.wait import WebDriverWait


def test_1(driver):
    driver.get('https://www.bbc.com/sport')

    img_locator = '//*[@id="main-content"]/div[4]/div/div/ul/li[1]/div/div/div/div[2]/div/div/span/picture/img'

    img_element = driver.find_element(By.XPATH, img_locator)

    img_src = img_element.get_attribute('src')
    if img_src:
        print("Этот элемент является картинкой с URL:", img_src)
    else:
        print("Этот элемент не является картинкой")


def test_2(driver):
    driver.get('https://www.bbc.com/')

    logo_locator = '//*[@id="homepage-link"]'

    lgo_locator = driver.find_element(By.XPATH, logo_locator)

    img_href = lgo_locator.get_attribute('href')

    assert img_href == 'https://www.bbc.com/', "Элемент не является логотипом, который ведет на домашнюю страницу"


def test_3(driver):
    driver.get('https://www.bbc.com/')

    locator = '//*[@id="orb-header"]/div/nav[2]/ul/li[3]/a/span'

    button_element = driver.find_element(By.XPATH, locator)

    assert button_element.is_displayed(), "Кнопка не отображается на странице"

    button_element.click()


def test_4(driver):
    driver.get('https://www.bbc.com/')

    locator_sport = '//*[@id="orb-header"]/div/nav[2]/ul/li[3]/a/span'

    sport_button_1 = driver.find_element(By.XPATH, locator_sport)

    assert sport_button_1.is_displayed(), "Кнопки 'Спорт' нет на странице"

    sport_button_1.click()

    WebDriverWait(driver, 10).until(url_to_be('https://www.bbc.com/sport'))

    current_url = driver.current_url

    expected_url = 'https://www.bbc.com/sport'
    assert current_url == expected_url, "Страница 'Спорт' не открывается"


def test_5(driver):
    driver.get('https://www.bbc.com/news')

    war_locator = '//*[@id="orb-modules"]/header/div[2]/div/div[1]/nav/ul/li[2]/a/span'
    climate_locator = '//*[@id="orb-modules"]/header/div[2]/div/div[1]/nav/ul/li[3]/a'
    bussines_locator = '//*[@id="orb-modules"]/header/div[2]/div/div[1]/nav/ul/li[7]/a'
    science_locator = '//*[@id="orb-modules"]/header/div[2]/div/div[1]/nav/ul/li[9]/a'
    arts_locator = '//*[@id="orb-modules"]/header/div[2]/div/div[1]/nav/ul/li[10]/a'

    element_1 = driver.find_element(By.XPATH, war_locator)
    element_1.click()
    driver.back()

    element_2 = driver.find_element(By.XPATH, climate_locator)
    element_2.click()
    driver.back()

    element_3 = driver.find_element(By.XPATH, bussines_locator)
    element_3.click()
    driver.back()

    element_4 = driver.find_element(By.XPATH, science_locator)
    element_4.click()
    driver.back()

    element_5 = driver.find_element(By.XPATH, arts_locator)
    element_5.click()
    driver.back()


def test_6(driver):
    driver.get('https://www.bbc.com/news')

    css_locator = "[class='gs-c-promo-image gs-u-mb gs-u-mb0@xs gs-u-float-right@m gel-2/3@m gs-u-display-block']"

    try:
        img_element = driver.find_element(By.CSS_SELECTOR, css_locator)
        img_src = img_element.get_attribute('src')
        print("Этот элемент является картинкой с URL:", img_src)
    except NoSuchElementException:
        print("Элемент не найден на странице")


def test_7(driver):
    driver.get('https://www.bbc.com/news')

    element_hd = "[id='homepage-link']"

    try:
        element_hd = driver.find_element(By.CSS_SELECTOR, element_hd)
        print("Элемент найден на странице")
    except NoSuchElementException:
        print("Элемент не найден на странице")

def test_8(driver):
    driver.get('https://www.bbc.com/news')

    element_sport = '[class="orbit-header-links international"] a[href="https://www.bbc.com/sport"]'

    try:
        element_spt = driver.find_element(By.CSS_SELECTOR, element_sport)
        print("Элемент найден на странице")
    except NoSuchElementException:
        print("Элемент не найден на странице")


def test_9(driver):
    driver.get('https://www.bbc.com/news')

    element_but = 'li.orb-nav-sport a[href="https://www.bbc.com/sport"]'

    try:
        element_sport = driver.find_element(By.CSS_SELECTOR, element_but)
        element_sport.click()
        print("Элемент найден и был нажат")
    except NoSuchElementException:
        print("Элемент не найден на странице")


def test_10(driver):
    driver.get('https://www.bbc.com/news')

    locators = [
        ('div.nw-o-news-wide-navigation a[href="/news/world"] > span', 'World'),
        ('div.nw-o-news-wide-navigation a[href="/news/science-environment-56837908"] > span', 'Climate'),
        ('div.nw-o-news-wide-navigation a[href="/news/uk"] > span', 'UK'),
        ('div.nw-o-news-wide-navigation a[href="/news/business"] > span', 'Business'),
        ('div.nw-o-news-wide-navigation a[href="/news/technology"] > span', 'Tech')
    ]

    for locator, label in locators:
        try:
            element = driver.find_element(By.CSS_SELECTOR, locator)
            if element.is_enabled():
                element.click()
                print(f"Кликнули на ссылку '{label}'")
            else:
                print(f"Ссылка '{label}' не кликабельна")
        except NoSuchElementException:
            print(f"Ссылка '{label}' не найдена")
        except ElementNotInteractableException:
            print(f"Ссылка '{label}' не кликабельна")

