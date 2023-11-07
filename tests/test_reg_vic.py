import time

from pages.registration_vik import RegistrationPage
from data import data_interaction
class TestRegistration():

    page = RegistrationPage

    def test_reg_vic(self, driver):

        page = RegistrationPage(driver, 'https://victoretc.github.io/selenium_waits/')
        page.open_browser()
        text = page.test_registration()
        assert text == 'Вы успешно зарегистрированы!', f'expected result: Вы успешно зарегистрированы! but got {text}'
