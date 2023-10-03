from elements import FiveElement


def test_page(driver):
    check = FiveElement(driver)
    check.open()
    check.clk()
    check.assert_main()
