from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators import Locators
from Diplom_3.curl import FEED_URL, PROFILE_URL, ORDER_HISTORY_URL
from allure import step
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FeedPage(BasePage):
    @step("Инициация класса")
    def __init__(self, driver):
        super().__init__(driver, FEED_URL)
        self.locators = Locators.feed_page

    @step("Открыть страницу Лента заказов /feed")
    def open_feed_page(self):
        self.open()

    # нажатие на один из заказов
    @step("Клик на один из заказов")
    def click_order_item(self):
        self.click_element(self.locators.ORDER_ITEM)

    # отображение модального окна заказа
    @step("Проверка отображения модального окна")
    def is_order_details_modal_visible(self):
        return self.is_element_visible(self.locators.ORDER_DETAILS_MODAL)

    # Отображение текста Состав - используется в ожиданиях
    @step("Проверка отображения текста Состав")
    def is_order_composition_text_visible(self):
        return self.is_element_visible(self.locators.ORDER_COMPOSITION_TEXT)

    @step("Получить текст поля Выполнено за всё время")
    def get_all_orders_count(self):
        return self.get_element_text(self.locators.ALL_ORDERS_COUNT)

    @step("Получить текст поля Выполнено за сегодня")
    def get_today_orders_count(self):
        return self.get_element_text(self.locators.TODAY_ORDERS_COUNT)

    @step("Получить текст (№) заказа В работе")
    def get_in_progress_order_id(self, order_id):
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element(Locators.feed_page.IN_PROGRESS_ORDER_ID, str(order_id)))
        return self.get_element_text(self.locators.IN_PROGRESS_ORDER_ID)

    @step("открыть страницу профиля /profile")
    def open_profile_page(self):
        self.find_element(self.locators.button_personal_area).click()

    @step("Клик на кнопку Личный кабинет")
    def click_personal_cabinet_button(self):
        self.click_element(self.locators.PERSONAL_CABINET_BUTTON)
        WebDriverWait(self.driver,10).until(EC.url_to_be(PROFILE_URL))

    @step("Клик на кнопку История заказов")
    def click_order_history_link(self):
        self.click_element(self.locators.ORDER_HISTORY_LINK)
        WebDriverWait(self.driver, 10).until(EC.url_to_be(ORDER_HISTORY_URL))

    @step("Поиск последнего заказа в Ленте заказов")
    def find_order_in_feed_orders(self):
        orders = WebDriverWait(self.driver, 10).until(
          EC.presence_of_all_elements_located(self.locators.ORDER_IN_FEED_ORDERS))
        return orders

    @step("Поиск последнего заказа в Ленте заказов авторизованного пользователя")
    def find_order_in_personal_history(self):
        orders = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.locators.ORDER_IN_FEED_ORDERS))
        return orders
