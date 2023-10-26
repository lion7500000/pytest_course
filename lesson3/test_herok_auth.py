from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_add_del_elem(driver,wait):
    USERNAME = 'admin'
    PASSWORD = 'admin'
    auth = f'http://{USERNAME}:{PASSWORD}@the-internet.herokuapp.com/basic_auth'
    driver.get(auth)
