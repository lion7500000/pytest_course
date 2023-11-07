from pages.alert_page import AlertPage
from data.data_interaction import Data


class TestAlert():

    pages = AlertPage
    def test_click_alert_btn(self, driver):
        page = AlertPage(driver, Data.ALERT_PAGE)
        page.open_browser()
        #wait and click alert button
        page.click_alert_btn().click()
        #switch to alert and assert text
        alert = driver.switch_to.alert
        assert alert.text == 'You clicked a button', f'Expected result: You clicked a button, but got {alert.text} '
        alert.accept()

    def test_alert_btn_5sec(self, driver):
        pages = AlertPage(driver, Data.ALERT_PAGE)
        pages.open_browser()
        #wait and click alert button - 5sec
        pages.click_alert_btn_5sec().click()
        #wait alert
        pages.alert_is_present()
        alert = driver.switch_to.alert
        assert alert.text == 'This alert appeared after 5 seconds', (f'Expected result: This alert appeared after 5 '
                                                                     f'seconds, but got {alert.text}')
        alert.accept()

    def test_alert_confirm_cancel(self, driver):
        pages = AlertPage(driver, Data.ALERT_PAGE)
        pages.open_browser()
        # wait and click promt alert button
        pages.alert_promt_btn().click()
        # wait alert
        pages.alert_is_present()
        alert = driver.switch_to.alert
        assert alert.text == 'Do you confirm action?', (f'Expected result: Do you confirm action?,but got {alert.text}')
        #cancel alrt
        alert.dismiss()

    def test_alert_confirm_ok(self, driver):
        pages = AlertPage(driver, Data.ALERT_PAGE)
        pages.open_browser()
        # wait and click promt alert button
        pages.alert_promt_btn().click()
        # wait alert
        pages.alert_is_present()
        alert = driver.switch_to.alert
        assert alert.text == 'Do you confirm action?', (f'Expected result: Do you confirm action?,but got {alert.text}')
        #cancel alrt
        alert.accept()

    def test_promt_alert(self, driver):
        pages = AlertPage(driver, Data.ALERT_PAGE)
        pages.open_browser()
        # wait and click promt alert button
        pages.promt_alert_btn().click()
        # wait alert
        pages.alert_is_present()
        alert = driver.switch_to.alert
        assert alert.text == 'Please enter your name', (f'Expected result: Please enter your name,but got {alert.text}')
        text = 'Hi my friend' #check text in page/alert.py too
        alert.send_keys(text)
        alert.accept()
        #wait for entered text and assert it
        pages.promt_text_assert()






