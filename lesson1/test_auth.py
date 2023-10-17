import locators
import data

def test_login_form(driver,log_in):
    cur_url = driver.current_url
    assert cur_url == locators.MAIN_PAGE, f'expected result {locators.MAIN_PAGE}, but got {log_in} '


def test_wron_Login(driver):
    driver.get(data.BASE_URL)
    user_fild2 = driver.find_element(*data.USER_FILD)
    pass_fild2 = driver.find_element(*data.PASSWORD_FILD)
    user_fild2.send_keys("user")
    pass_fild2.send_keys("user")
    driver.find_element(*data.LOGIN_BTN).click()

    error = driver.find_element(*locators.ERROR_MES).text
    assert error == locators.ERROR_TXT, f'expected result {locators.ERROR_TXT}, but got {error} '










