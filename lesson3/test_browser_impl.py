from selenium.webdriver.common.by import By
def test_browsert(driver):
    driver.get("https://victoretc.github.io/selenium_waits/")
    text = driver.find_element(By.CSS_SELECTOR, "body h1").text
    assert text == 'Практика с ожиданиями в Selenium'
    button = (driver.find_element(By.ID, "startTest"))
    assert button.is_enabled()
    button.click()
    reg_btn_text = (driver.find_element(By.ID, 'register')).text
    assert reg_btn_text == 'Зарегистрироваться'
    login_fild = (driver.find_element(By.ID, 'login')).send_keys('login')
    password_fild = (driver.find_element(By.ID, 'password')).send_keys('password')
    check_box =(driver.find_element(By.ID, 'agree')).click()
    reg_btn = (driver.find_element(By.ID, 'register')).click()
    reg_text_clc = (driver.find_element(By.CSS_SELECTOR, 'p[id ="successMessage"]')).click()
    reg_text = (driver.find_element(By.CSS_SELECTOR, 'p[id ="successMessage"]')).text
    assert reg_text == 'Вы успешно зарегистрированы!'