import allure

from elements.hw_25_element import HW25

@allure.feature('Simple Alert')
@allure.severity('critical')
@allure.story('Checking the work of Simple Alert')
def test_simple_alert(driver):
    """
    Work simple alert
    """
    simple_alert = HW25(driver)
    simple_alert.open()
    simple_alert.clk()
    simple_alert.clk_simple_alert()
    simple_alert.use_simple_alert()

@allure.feature('Confirm Alert')
@allure.severity('minor')
@allure.story('Checking the work of Confirm Alert')
def test_confirm_alert(driver):
    """
    Work confirm alert
    """
    simple_alert = HW25(driver)
    simple_alert.open()
    simple_alert.clk()
    simple_alert.clk_simple_alert()
    simple_alert.use_simple_alert()

@allure.feature('Confirm Alert dismiss')
@allure.severity('normal')
@allure.story('Checking the work of Confirm Alert dismiss')
def test_confirm_dissmis_alert(driver):
    """
    Work confirm alert and click dismiss
    """
    simple_alert = HW25(driver)
    simple_alert.open()
    simple_alert.clk()
    simple_alert.clk_simple_alert()
    simple_alert.use_dissmis()


@allure.feature('Prompt Alert')
@allure.severity('normal')
@allure.story('Checking the work of Prompt Alert')
def test_prompt_alert(driver):
    """
    Work prompt alert
    """
    prompt_alert = HW25(driver)
    prompt_alert.open()
    prompt_alert.clk()
    prompt_alert.clk_promt_alert()
    prompt_alert.use_prompt_alert()

@allure.feature('Prompt Alert dismiss')
@allure.severity('minor')
@allure.story('Checking the work of Prompt Alert dismiss')
def test_prompt_dismiss_alert(driver):
    """
    Work prompt alert and click dismiss
    """
    prompt_alert = HW25(driver)
    prompt_alert.open()
    prompt_alert.clk()
    prompt_alert.clk_promt_alert()
    prompt_alert.use_dissmis()

@allure.feature('New window')
@allure.severity('minor')
@allure.story('Checking the work of open new window')
def test_window(driver):
    """
    open the page in a new window
    """
    check_new_window = HW25(driver)
    check_new_window.open()
    check_new_window.open_window()


@allure.feature('Iframe')
@allure.severity('blocker')
@allure.story('We look for a frame and check the text in it')
def test_iframe(driver):
    """
    found iframe on the page
    """
    found_iframe = HW25(driver)
    found_iframe.open()
    found_iframe.clk_frame()
    found_iframe.clk_iframe()
    found_iframe.check_text()

@allure.feature('Download file')
@allure.severity('blocker')
@allure.story('Check downloading a file from the site')
def test_download_file(driver):
    """
    download file
    """
    download_file = HW25(driver)
    download_file.open()
    download_file.clk_download()
    download_file.assert_dow()

@allure.feature('Upload file')
@allure.severity('blocker')
@allure.story('Check the file upload to the site')
def test_upload_file(driver):
    """
    upload_file
    """
    upload_file = HW25(driver)
    upload_file.open()
    upload_file.clk_upload()
    upload_file.assert_upl()
