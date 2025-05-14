from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators import Locators
from Diplom_3.curl import CONSTRUCTOR_URL, FEED_URL, INGREDIENT_DETAILS_URL
from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import url_to_be
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, CONSTRUCTOR_URL) #Start from main page
        self.locators = Locators.main_page

    def open_main_page(self):
        self.open()
        WebDriverWait(self.driver, 10).until(EC.url_to_be(CONSTRUCTOR_URL))

    def click_constructor_button(self):
        self.click_element(self.locators.CONSTRUCTOR_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.url_to_be(CONSTRUCTOR_URL))


    def click_feed_button(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locators.FEED_BUTTON))
        #botton.click()
        sleep(2)
        self.click_element(self.locators.FEED_BUTTON)
    #    WebDriverWait(self.driver, 10).until(EC.url_to_be(FEED_URL))

    def click_ingredient(self):
        botton = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.locators.INGREDIENT_BUN))
        botton.click()
        #self.click_element(self.locators.INGREDIENT_BUN)


    def close_ingredient_modal(self):
        self.click_element(self.locators.INGREDIENT_MODAL_CLOSE_BUTTON)

    def is_ingredient_modal_visible(self):
        return self.is_element_visible(self.locators.INGREDIENT_MODAL)

    def is_ingredient_modal_not_visible(self):
        return self.is_element_not_visible(self.locators.INGREDIENT_MODAL)

    def drag_ingredient_to_order(self):
        source_element = self.find_element(self.locators.INGREDIENT_BUN)
        target_element = self.find_element(self.locators.ORDER_INGREDIENT)
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    def click_order_button(self):
        self.click_element(self.locators.ORDER_BUTTON)

    def is_order_modal_visible(self):
        return self.is_element_visible(self.locators.ORDER_MODAL)

    def is_order_id_text_visible(self):
        return self.is_element_visible(self.locators.ORDER_ID_TEXT)

    def find_counter(self):
        return self.find_element(self.locators.INGREDIENT_COUNTER)

