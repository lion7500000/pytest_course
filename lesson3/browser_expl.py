from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
def test_browsert(driver,wait):
    driver.get("https://victoretc.github.io/selenium_waits/")
    text = driver.find_element(By.CSS_SELECTOR, "body h1").text
    assert text == 'Практика с ожиданиями в Selenium'
    button = wait.until(EC.element_to_be_clickable((By.ID, "startTest")))
    button.click()
    reg_btn_text = (driver.find_element(By.ID, 'register')).text
    assert reg_btn_text == 'Зарегистрироваться'
    login_fild = (driver.find_element(By.ID, 'login')).send_keys('login')
    password_fild = (driver.find_element(By.ID, 'password')).send_keys('password')
    check_box =(driver.find_element(By.ID, 'agree')).click()
    reg_btn = (driver.find_element(By.ID, 'register')).click()
    text_succes = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'p[id ="successMessage"]'),"Вы успешно зарегистрированы!"))
    reg_text = (driver.find_element(By.CSS_SELECTOR, 'p[id ="successMessage"]')).text
    assert reg_text == 'Вы успешно зарегистрированы!'