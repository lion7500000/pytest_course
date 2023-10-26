from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_add_del_elem(driver,wait):
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
    wait_loc = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[onclick="addElement()"]')))
    add_elem_butt = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    add_elem_butt.click()
    del_butt = driver.find_element(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')
    del_butt.click()