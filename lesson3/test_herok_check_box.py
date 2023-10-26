from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_check_box(driver,wait):

    CHECK_BOX = (By.CSS_SELECTOR, 'input[type="checkbox"]')

    driver.get('https://the-internet.herokuapp.com/checkboxes')
    check_boxes = driver.find_elements(*CHECK_BOX)
    assert check_boxes[1].is_selected(), "Checkbox 1 is not checked by default"
    check_boxes[0].click()
    assert check_boxes[0].is_selected() and check_boxes[1].is_selected(), "Checkbox 1 and 2 are checked "
    check_boxes[1].click()
    assert check_boxes[0].is_selected() and not check_boxes[1] .is_selected(), "Checkbox 1 checked and Checkbox 2 is not checked"

