# Личный кабинет
import allure
from Diplom_3.pages.base_page import BasePage
from Diplom_3.curl import BASE_URL, PROFILE_URL, LOGIN_URL, ORDER_HISTORY_URL
from Diplom_3.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, BASE_URL)
        self.locators = Locators.profile_page

    @allure.step("открыть страницу профиля /profile через UI")
    def open_profile_page(self):
        self.open()

    @allure.step("Клик на кнопку Личный кабинет") #
    def click_personal_cabinet_button(self):
        self.click_element(self.locators.PERSONAL_CABINET_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.url_to_be(PROFILE_URL))

    @allure.step("Клик на кнопку История заказов")
    def click_order_history_link(self):
        self.click_element(self.locators.ORDER_HISTORY_LINK)
        WebDriverWait(self.driver, 10).until(EC.url_to_be(ORDER_HISTORY_URL))

    @allure.step("Клик по кнопке Выйти")
    def click_logout_button(self):
        self.click_element(self.locators.LOGOUT_BUTTON)
        WebDriverWait(self.driver, 5).until(EC.url_to_be(LOGIN_URL))

    @allure.step("Проверка нахождения на странице /login")
    def is_redirected_to_login_page(self, driver):
        return driver.current_url == LOGIN_URL

    @allure.step("Проверка нахождения на странице /order-history")
    def is_redirected_to_order_history_page(self, driver):
        return driver.current_url == ORDER_HISTORY_URL