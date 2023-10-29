# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from locators.locators_interactions import Locators
from pages.base_page import Page
from pages.interactions_page import InteractionPage

class TestInteractions():

    page = InteractionPage

    def test_drop_simpl(self, driver):

        page = InteractionPage(driver, 'https://demoqa.com/droppable')
        page.open_browser()

        text_drop = page.inter_drag_drop()
        assert text_drop == "Dropped!", f'expected result: Dropped! but got {text_drop}'

    def test_drop_accept(self, driver):

         page = InteractionPage(driver, 'https://demoqa.com/droppable')
         page.open_browser()

         text_drop = page.accept_drag_drop()
         # assert text_drop == "Dropped!", f'expected result: Dropped! but got {text_drop}'
