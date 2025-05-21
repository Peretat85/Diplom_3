# тесты Личного кабинета
from Diplom_3.pages.profile_page import ProfilePage
from Diplom_3.curl import LOGIN_URL, PROFILE_URL, ORDER_HISTORY_URL
from allure import title


class TestProfile:
    @title("Переход по клику на 'Личный кабинет' авторизованного пользователя")
    # Предусловие: залогиниться, автоматически перебросит на главную
    def test_go_to_personal_cabinet(self, upload_token_to_session, driver):  #  работает в GC
        profile_page = ProfilePage(driver)

        # Кликаем по кнопке Личный кабинет
        profile_page.click_personal_cabinet_button()
        profile_page.page_refresh()

        # Ожидаем перехода на страницу профиля account/profile
        assert profile_page.get_current_url() == PROFILE_URL, "Не удалось загрузить 'Личный кабинет' авторизованного пользователя"

    @title("Переход в раздел «История заказов»:")
    # Предусловие: залогиниться, автоматически перебросит на главную
    def test_go_to_order_history(self, upload_token_to_session, driver):
        # 1. Кликаем по кнопке "личный кабинет", т.к. к этой странице нет доступа непосредственно через url
        profile_page = ProfilePage(driver)
        profile_page.click_personal_cabinet_button()
        # 2. Ждем загрузки страницы

        # 3. Нажать на История заказов
        profile_page.click_order_history_link()
        profile_page.page_refresh()
        # Ожидаем: переход на страницу истории заказов /account/order-history
        assert profile_page.get_current_url() == ORDER_HISTORY_URL, "Страница 'История заказов' не загрузилась"

    @title("Выход из аккаунта")
    # Предусловие: залогиниться, автоматически перебросит на главную
    def test_logout(self, upload_token_to_session, driver):
        # 1. Кликаем по кнопке "личный кабинет"
        profile_page = ProfilePage(driver)
        profile_page.click_personal_cabinet_button()

        # 2. нажать кнопку Выход
        profile_page.click_logout_button()
        profile_page.page_refresh()
        # Ожидаем: переход на страницу входа /login
        assert profile_page.get_current_url() == LOGIN_URL, "Страница 'Выход из аккаунта' не загрузилась"