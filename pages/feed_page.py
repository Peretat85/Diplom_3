from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators import Locators
from Diplom_3.curl import FEED_URL, PROFILE_URL, ORDER_HISTORY_URL, ORDERS_API_URL
from allure import step
import requests

class FeedPage(BasePage):
    @step("Инициация класса")
    def __init__(self, driver):
        super().__init__(driver, FEED_URL)
        self.locators = Locators.feed_page

    @step("Открыть страницу Лента заказов /feed")
    def open_feed_page(self):
        self.open()

    @step("Клик на один из заказов")
    def click_order_item(self):
        self.click_element(self.locators.ORDER_ITEM)

    @step("Проверка отображения модального окна")
    def is_order_details_modal_visible(self):
        return self.is_element_visible(self.locators.ORDER_DETAILS_MODAL)

    # Отображение текста Состав - используется в ожиданиях
    @step("Проверка отображения текста Состав")
    def is_order_composition_text_visible(self):
        return self.is_element_visible(self.locators.ORDER_COMPOSITION_TEXT)

    @step("Получить текст поля Выполнено за всё время")
    def get_all_orders_count(self):
        return self.get_text_of_element(self.locators.ALL_ORDERS_COUNT)

    @step("Получить текст поля Выполнено за сегодня")
    def get_today_orders_count(self):
        return self.get_text_of_element(self.locators.TODAY_ORDERS_COUNT)

    # сделать отдельный метод для теста test_order_in_history_and_feed
    @step("Получить текст (№) заказа В работе= должно быть: получить локатор элемента по тексту")
    def get_in_progress_order_id(self, order_id):
        return self.get_text_of_element(self.locators.IN_PROGRESS_ORDER_ID, order_id)

    @step("открыть страницу профиля /profile")
    def open_profile_page(self):
        self.find_element(self.locators.button_personal_area).click()

    @step("Клик на кнопку Личный кабинет")
    def click_personal_cabinet_button(self):
        self.click_element(self.locators.PERSONAL_CABINET_BUTTON)

    @step("Клик на кнопку История заказов")
    def click_order_history_link(self):
        self.click_element(self.locators.ORDER_HISTORY_LINK)

    @step("Поиск последнего заказа в Ленте заказов")
    def find_order_in_feed_orders(self):
       return self.presence_all_element(self.locators.ORDER_IN_FEED_ORDERS)

    @step("Поиск последнего заказа в Ленте заказов авторизованного пользователя")
    def find_order_in_personal_history(self):
        return self.presence_all_element(self.locators.ORDER_IN_FEED_ORDERS)

    # Создание заказа здесь,
    # т.к. если вынести его в фикстуру,
    # то нельзя будет его использовать как шаг теста
    @step("Создание заказа")
    def create_order(self, upload_token_to_session):
        # 1. Создаем новый заказ
        order_data = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa73"]
        }
        headers = {
            "Authorization": upload_token_to_session
        }
        response = requests.post(ORDERS_API_URL, json=order_data, headers=headers)
        order_id = str(response.json().get("order", {}).get("number"))
        return order_id
