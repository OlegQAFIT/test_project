from elements import LoginForm


def test_login(driver):
    """
    Checking login form
    """

    check_login = LoginForm(driver)
    check_login.open()
    check_login.enter_username()
    check_login.enter_password()
    check_login.clk()
