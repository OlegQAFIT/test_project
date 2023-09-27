from elements import FooterElement
from pages import MainPage
from pages.contacts_page import ContactsPage


def test_1(driver):
    """
    From the drop-down list, try to select a silver subscription
    """
    check_text = MainPage(driver)
    check_text.open()
    check_text.clc()
    check_text.assert_main()


def test_2(driver):
    """
    We check on the contact page, the correct phone number
    """
    check_phone = ContactsPage(driver)
    check_phone.open()
    check_phone.clc()
    check_phone.assert_phone()


def test_3(driver):
    """
    We check in the documentation tab that there is a document with the name -"Индивидуальные лицензии"
    """
    found_text = FooterElement(driver)
    found_text.open()
    found_text.click_on_docs()
    found_text.assert_dok("Индивидуальные лицензии")


def test_4(driver):
    """
    Checking the form for sending a message for an offer
    """
    send_form = MainPage(driver)
    send_form.open()
    send_form.enter_email()
    send_form.clc_get_1()
    send_form.drop_clc()
    send_form.fill_form(
        send_form.email_locator,
        send_form.name_locator,
        send_form.phone_locator,
        send_form.city_locator,
        send_form.employe_locator
    )
    send_form.clc_get_2()
    send_form.assert_form()


def test_5(driver):
    """
    Checking social media links
    """
    soc_media = FooterElement(driver)
    soc_media.open()
    soc_media.click_on_instagram()
    soc_media.assert_instagram()
    soc_media.switch_to_main_window()
    soc_media.assert_linkedin()
