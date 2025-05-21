from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait
from allure import step

from Diplom_3.conftest import driver


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @step("Открыть страницу")
    def open(self):
        self.driver.get(self.url)

    @step("Поиск элемента по локатору")
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    @step("Ожидание кликабельности элемента и нажатие на него")
    def click_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator)).click()

    @step("Отправка ключа элементу")
    def send_keys_to_element(self, locator, value, time=10):
        element = self.find_element(locator, time)
        element.send_keys(value)

    @step("Получить текст элемента")
    def get_text_of_element(self, locator,  time=10):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(locator))
        element = self.find_element(locator, time)
        return element.text

    @step("Получить локатор элемента по его тексту")
    def get_element_text(self, locator, text, time=10):
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element(locator, text))
        element = self.find_element(locator, time)
        return element

    @step("Определить видимость элемента")
    def is_element_visible(self, locator, time=10):
        try:
            WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    @step("Определение невидимости элемента")
    def is_element_not_visible(self, locator, time=10):
        try:
            WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))
            return True
        except:
            return False

    @step("Проверка адреса текущей страницы")
    def get_current_url(self):
        return self.driver.current_url

    @step("Поиск всех элементов")
    def presence_all_element(self, element):
        orders = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(element))
        return orders

    @step("Обновление страницы")
    def page_refresh(self):
        self.driver.refresh()

    @step("Ждать загрузки страницы")
    def page_load(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))