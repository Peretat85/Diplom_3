# Раздел "Ленты заказов"
from Diplom_3.pages.feed_page import FeedPage
from Diplom_3.curl import(
    BASE_URL, LOGIN_URL, REGISTER_API_URL, LOGIN_API_URL,
    ORDERS_API_URL, FEED_URL, PROFILE_URL, ORDER_HISTORY_URL
)
import requests
from allure import title



class TestFeedPage:
    @title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    @title("Тест без авторизации")
    def test_order_details_modal(self, driver):
        # 1. Перейти в ленту заказов
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        # 2. Выбираем первый заказ на ленте
        feed_page.click_order_item()
        # Ожидаем: появление модального окна с надписью Состав
        assert feed_page.is_order_composition_text_visible()

    @title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    @title("Тест для авторизованного пользователя")
    # Предусловие залогиниться, автоматически перебросит на главную
    def test_order_details_modal_autoriz(self, upload_token_to_session, driver):
        # 1. Перейти в ленту заказов
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        # 2. Выбираем первый заказ на ленте
        feed_page.click_order_item()
        # Ожидаем: появление модального окна с надписью Состав
        assert feed_page.is_order_composition_text_visible()

    @title("Заказы пользователя из раздела 'История заказов' отображаются на странице 'Лента заказов'")
    # Предусловие: залогиниться
    def test_order_in_history_and_feed(self, upload_token_to_session, driver):
        # 1. Переход на страницу Лента заказов - загрузка страницы
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        # 2. создаем заказ и запоминаем его номер
        order_id = feed_page.create_order(upload_token_to_session)
        order_id_str = str(order_id)  # Приводим к строке

        # 3. Искать номер заказа в Ленте заказов (общей)
        feed_orders = feed_page.find_order_in_feed_orders()
        print("feed_orders =", feed_orders)
        feed_orders_text = [order.text[2:] for order in feed_orders]
        print("feed_orders_text =", feed_orders_text)
        # 4. Перейти на страницу /profile через UI
        feed_page.click_personal_cabinet_button()

        # 5. Нажать на История заказов
        feed_page.click_order_history_link()

        # 6. Искать номер заказа в списке заказов пользователя
        history_orders = feed_page.find_order_in_personal_history()  # поменять логику метода
        history_orders_text = [order.text[2:] for order in history_orders]

        # Ожидаем, что заказ отображается в Ленте заказов
        assert order_id_str in feed_orders_text, "Заказ не найден в Ленте заказов"
        # Ожидаем, что заказ отображается в Истории заказов
        assert order_id_str in history_orders_text, "Заказ не найден в Истории заказов"


    @title("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    # Предусловие: залогиниться
    def test_completed_orders_counter(self, upload_token_to_session, driver):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()

        # 1. Получаем текущее количество выполненных заказов
        all_orders_text = feed_page.get_all_orders_count()
        all_orders_count = int(all_orders_text)

        # 3. Обновляем страницу
        feed_page.page_refresh()

        # 4. Создаем заказ
        feed_page.create_order(upload_token_to_session)

        # 5. Получаем текущее количество выполненных заказов
        new_all_orders_text = feed_page.get_all_orders_count()
        new_all_orders_count = int(new_all_orders_text)

        # Ожидаем: количество заказов увеличилось
        assert new_all_orders_count > all_orders_count, "Количество всех заказов не увеличилось"


    @title("При создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_today_orders_count_increases(self, upload_token_to_session, driver):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()

        # 1. Получаем текущее количество выполненных заказов за сегодня
        today_orders_text = int(feed_page.get_today_orders_count())
        today_orders = int(today_orders_text)

        # 2. Создаем новый заказ
        feed_page.create_order(upload_token_to_session)

        # 3. Обновляем страницу
        feed_page.page_refresh()

        # 4. Получаем текущее количество выполненных заказов за сегодня
        new_today_orders_text = feed_page.get_today_orders_count()
        new_today_orders = int(new_today_orders_text)

        # Ожидаем: количество заказов увеличилось
        assert new_today_orders > today_orders, "Количество заказов за сегодня не увеличилось"


    @title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_in_progress(self, upload_token_to_session, driver):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()

        # 2. Обновляем страницу
        feed_page.page_refresh()

        # 3. Запоминаем номер заказа
        order_id = "0"+feed_page.create_order(upload_token_to_session)

        # 4. Запоминаем текст последнего заказа "В работе"
        in_progress_order_id = feed_page.get_in_progress_order_id(order_id)

        # Ожидаем: номер заказа = тексту последнего заказа ленты В работе
        assert order_id == in_progress_order_id, "Заказ не найден в разделе 'В работе'"