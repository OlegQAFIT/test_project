from elements import SubmitForm


def test_2(driver):
    """
        Checking registration
        """
    regist_form = SubmitForm(driver)
    regist_form.open()
    regist_form.enter_first_name()
    regist_form.enter_last_name()
    regist_form.enter_phone()
    regist_form.enter_email()
    regist_form.enter_address()
    regist_form.enter_city()
    regist_form.enter_state_province()
    regist_form.enter_postal_code()
    regist_form.enter_user_name()
    regist_form.enter_password()
    regist_form.enter_confirm_password()
    regist_form.clk()
    regist_form.assert_reg("Dear Oleg Atrokhau")
