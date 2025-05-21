from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators import Locators
from Diplom_3.curl import CONSTRUCTOR_URL, FEED_URL, INGREDIENT_DETAILS_URL
from selenium.webdriver import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from allure import step

class MainPage(BasePage):
    @step("Инициация класса Главная страница")
    def __init__(self, driver):
        super().__init__(driver, CONSTRUCTOR_URL) #Start from main page
        self.locators = Locators.main_page

    @step("Открыть страницу Конструктор")
    def open_main_page(self):
        self.open()
        self.page_load(CONSTRUCTOR_URL)

    @step("Нажатие на кнопку Конструктор")
    def click_constructor_button(self):
        self.click_element(self.locators.CONSTRUCTOR_BUTTON)

    @step("Клик по кнопке Лента заказов")
    def click_feed_button(self):
        self.presence_all_element(self.locators.FEED_BUTTON)
        self.click_element(self.locators.FEED_BUTTON)

    @step("Клик по ингредиенту")
    def click_ingredient(self):
        self.click_element(self.locators.INGREDIENT_BUN)

    @step("Закрыть модальное окно")
    def close_ingredient_modal(self):
        self.click_element(self.locators.INGREDIENT_MODAL_CLOSE_BUTTON)

    @step("Модальное окно отображается")
    def is_ingredient_modal_visible(self):
        return self.is_element_visible(self.locators.INGREDIENT_MODAL)

    @step("Модальное окно не отображается")
    def is_ingredient_modal_not_visible(self):
        return self.is_element_not_visible(self.locators.INGREDIENT_MODAL)

    @step("Перетаскивание ингредиентов")
    def drag_ingredient_to_order(self):
        source_element = self.find_element(self.locators.INGREDIENT_BUN)
        target_element = self.find_element(self.locators.ORDER_INGREDIENT)
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    @step("Клик по кнопке заказов")
    def click_order_button(self):
        self.click_element(self.locators.ORDER_BUTTON)

    @step("Окно заказа отображается")
    def is_order_modal_visible(self):
        return self.is_element_visible(self.locators.ORDER_MODAL)

    @step("№ заказа отображается в окне заказов")
    def is_order_id_text_visible(self):
        return self.is_element_visible(self.locators.ORDER_ID_TEXT)

    @step("Поиск количества добавленного ингредиента")
    def find_counter(self):
        # element = self.find_element(self.locators.INGREDIENT_COUNTER)
        # return element.text
        return self.get_text_of_element(self.locators.INGREDIENT_COUNTER)


