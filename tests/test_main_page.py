# Проверка основного функционала

from Diplom_3.pages.main_page import MainPage
from Diplom_3.curl import CONSTRUCTOR_URL, FEED_URL, INGREDIENT_DETAILS_URL
from allure import title

@title("Проверка основного функционала")
class TestMainPage:

    @title("Переход на Конструктор")
    def test_click_constructor_button(self, driver): # работает в GC
        # 1. Открыть главную страницу
        main_page = MainPage(driver)
        main_page.open_main_page()
        # 2. Нажать на Лента заказов
        main_page.click_feed_button()
        # 3. Убедиться, что перешли на Ленту заказов
        assert main_page.get_current_url()== FEED_URL
        # 4. Нажать на Конструктор
        main_page.click_constructor_button()
        # 5. Ожидаем: переход на страницу Конструктор
        assert main_page.get_current_url() == CONSTRUCTOR_URL

    @title("Переход на ленту заказов")
    def test_click_feed_button(self,driver): # работает в GC
        # 1. Открыть главную страницу
        main_page = MainPage(driver)
        main_page.open_main_page()
        # 2. Нажать на Лента заказов
        main_page.click_feed_button()
        # 3. Ожидаем: переход на страницу Лента заказов
        assert main_page.get_current_url() == FEED_URL

    @title("Клик по ингредиенту открывает информацию дополнительном окне")
    def test_open_ingredient_details_modal(self, driver): # работает в GC
        # 1. Открыть главную страницу
        main_page = MainPage(driver)
        main_page.open_main_page()
        # 2. Кликнуть на ингредиент
        main_page.click_ingredient()
        # 3. Ожидаем: модальное окно ингредиента отобразилось
        assert main_page.is_ingredient_modal_visible()

    @title("Дополнительное окно закрывается при нажатии на крестик")
    def test_close_ingredient_details_modal(self, driver): # работает в GC
        # 1. Открыть главную страницу
        main_page = MainPage(driver)
        main_page.open_main_page()
        # 2. Кликнуть на ингредиент
        main_page.click_ingredient()
        # 3. Убедиться, что модальное окно ингредиента отобразилось
        assert main_page.is_ingredient_modal_visible()
        # 4. Нажать на крестик
        main_page.close_ingredient_modal()
        # Ожидаем: модальное окно пропало
        assert main_page.is_ingredient_modal_not_visible()


@title("Тесты на заказ")
class TestOrderMainPage:

    @title(" При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_place_order_logged_in(self, driver):
        # 1. на главную страницу
        main_page = MainPage(driver)
        main_page.open_main_page()
        # 2. добавить (перетянуть) ингредиенты в заказ
        main_page.drag_ingredient_to_order()
        # 3. убедиться, что у ингредиента цифра >0
        counter = main_page.find_counter()
        assert counter == "2"

    @title("Авторизованный пользователь может оформить заказ")
    # Предусловие: залогиниться, автоматически перебросит на главную
    def test_logged_user_make_order_Log_us(self, upload_token_to_session, driver):  #  работает в GC
        # 1. На главную страницу
        main_page = MainPage(driver)
        main_page.open_main_page()
        # 2. добавить (перетянуть) ингредиенты в заказ
        main_page.drag_ingredient_to_order()

        # 3. нажать на кнопку Оформить заказ
        main_page.click_order_button()

        # 4. ожидать появления модального окна и сообщения c идентификатором заказа
        assert main_page.is_order_modal_visible()
        assert main_page.is_order_id_text_visible()