# Восстановление пароля - ok
from Diplom_3.pages.recovery_password_page import LoginPage, ForgotPasswordPage
from Diplom_3.curl import FORGOT_PASSWORD_URL, RESET_PASSWORD_URL
from Diplom_3.locators import Locators
from allure import title

EMAIL = "qwerty@mail.ru"# тестовый пароль

class TestPasswordReset:
    @title("Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    def test_navigate_to_forgot_password(self, driver): # + GH
        # 1. загрузка страницы входа
        login_page = LoginPage(driver)
        login_page.open_login_page()

        # 2. Нажать кнопку Восстановить пароль
        login_page.click_forgot_password_link()

        # Ожидание: переход на страницу https://stellarburgers.nomoreparties.site/forgot-password
        assert login_page.get_current_url() == FORGOT_PASSWORD_URL

    @title("Переход на страницу восстановления пароля /reset-password при вводе почты и клику по кнопке Восстановить")
    def test_enter_email_and_click_reset(self, driver): # не работает в Firefox без sleep
        # 1. переход на страницу восстановить пароль https://stellarburgers.nomoreparties.site/forgot-password
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_forgot_password_page()
        # ждем загрузку кнопки Восстановить
        forgot_password_page.is_reset_button_displayed()
        # 2. ввести почту
        forgot_password_page.enter_email(EMAIL)
        # 3. нажать кнопку Восстановить
        forgot_password_page.click_reset_button()

        # Ожидаем перехода на страницу https://stellarburgers.nomoreparties.site/forgot-password
        assert forgot_password_page.get_current_url() == RESET_PASSWORD_URL

    @title("Проверка подсветки поля пароль на странице /reset-password при щелчке на 'глазик' ")
    def test_show_password_button(self, driver): # придумать ожидания для Firefox
        # Предусловие1: выполнение перехода на страницу восстановления пароля
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_forgot_password_page()
        # ждем загрузку кнопки Восстановить
        forgot_password_page.is_reset_button_displayed()
        # Предусловие2: ввести почту
        forgot_password_page.enter_email(EMAIL)
        # Предусловие3: нажать кнопку Восстановить - переход на страницу /eset-password
        forgot_password_page.click_reset_button()
        # 1. Кликнуть на кнопку показа пароля (глазик)
        forgot_password_page.click_show_password_button()
        # 2. Определить атрибуты поля ввода пароля
        password_input = forgot_password_page.password_attribute() # сработало, отправить локатор в локаторы, здесь ставить ссылку
        # Ожидаем, что поле ввода пароля подсветится рамкой - проверяем свойство input_status_active поля ввода пароля
        assert Locators.ACTIVE_CLASS in password_input.get_attribute("class"), "Поле пароля не стало активным"
