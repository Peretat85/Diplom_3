from Diplom_3.pages.base_page import BasePage
from Diplom_3.curl import BASE_URL, LOGIN_URL, FORGOT_PASSWORD_URL, RESET_PASSWORD_URL
from Diplom_3.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from allure import step

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, LOGIN_URL)  # заменить страницу на ту где кнопка Восстановить
        self.locators = Locators.login_page

    @step ( "Открыть страницу авторизации  /login")
    def open_login_page(self):
        self.open()
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.locators.FORGOT_PASSWORD_LINK))

    @step ("Нажатие на кнопку Восстановить пароль")
    def click_forgot_password_link(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.locators.FORGOT_PASSWORD_LINK))
        self.click_element(self.locators.FORGOT_PASSWORD_LINK)
        WebDriverWait(self.driver,5).until(EC.url_to_be(FORGOT_PASSWORD_URL))

    @step ("Ввод почты")
    def enter_email(self, email):
        self.send_keys_to_element(self.locators.EMAIL_INPUT, email)

    @step("Ввод пароля")
    def enter_password(self, password):
       ## self.send_keys_to_element(self.locators.PASSWORD_INPUT, password)
        password_field = self.find_element(self.locators.PASSWORD_INPUT)
        password_field.send_keys(password)
        password_field.send_keys(Keys.TAB)

    @step("Нажать кнопку Войти")
    def click_login_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.locators.LOGIN_BUTTON))
        self.click_element(self.locators.LOGIN_BUTTON)

    @step("Перейти на страницу регистрации")
    def is_redirected_to_profile_page(self, driver):
        return driver.current_url == PROFILE_URL

    @step("Перейти на страницу регистрации")
    def is_redirected_to_login_page(self, driver):
        return driver.current_url == LOGIN_URL

    @step("Нажать на кнопку Личный кабинет")
    def click_personal_cabinet_button_main(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.locators.PERSONAL_CABINET_BUTTON))
        self.click_element(self.locators.PERSONAL_CABINET_BUTTON)


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, FORGOT_PASSWORD_URL)
        self.locators = Locators.forgot_password_page

    @step("Открыть страницу восстановления  /forgot-pass")
    def open_forgot_password_page(self):
        self.open()
        WebDriverWait(self.driver,5).until(EC.url_to_be(FORGOT_PASSWORD_URL))


    @step("Ввести e-mail")
    def enter_email(self, email):
        email_field = self.find_element(self.locators.EMAIL_INPUT)
        email_field.send_keys(email)
        email_field.send_keys(Keys.TAB)  # После ввода нажать Tab

    @step("Нажать кнопку Восстановить")
    def click_reset_button(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators.RESET_BUTTON)) # снять фокус с поля почты
        self.click_element(self.locators.RESET_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.url_to_be(RESET_PASSWORD_URL))

    @step("Ждать видимости кнопки Восстановить")
    def is_reset_button_displayed(self):
        return self.is_element_visible(self.locators.RESET_BUTTON)

    def is_redirected_to_reset_password_page(self, driver):
        return self.driver.current_url == RESET_PASSWORD_URL

    @step("Найти элемент с локатором {locator}")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @step("Кликнуть в окно ввода пароля")
    def click_show_password_button(self):
        self.find_element(self.locators.SHOW_PASSWORD_BUTTON)
        self.click_element(self.locators.SHOW_PASSWORD_BUTTON)

    @step("Определить атрибуты поля ввода пароля")
    def password_attribute(self):
        element = self.find_element(self.locators.PASSWORD_FIELD)
        return element
