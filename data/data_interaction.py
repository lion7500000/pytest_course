from selenium.webdriver.common.by import By

class Data:

    BASE_URL = "https://www.saucedemo.com/"
    USER_FILD = (By.ID, "user-name")
    PASSWORD_FILD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    LOGIN = "standard_user"
    PASSWORD = "secret_sauce"
    FIRST_NAME = "Jon"
    LAST_NAME = "Smit"
    ZIP_COD = "9045"
    CHECK_OUT_TXT = "Checkout: Your Information"
    CHECK_OUT_TXT2 = "Checkout: Overview"
    CHECK_OUT_COMP_TXT = "Checkout: Complete!"
    ALERT_PAGE = 'https://demoqa.com/alerts'