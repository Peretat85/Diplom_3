from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def click_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator)).click()

    def send_keys_to_element(self, locator, value, time=10):
        element = self.find_element(locator, time)
        element.send_keys(value)

    def get_element_text(self, locator, time=10):
        element = self.find_element(locator, time)
        return element.text

    def is_element_visible(self, locator, time=10):
        try:
            WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def is_element_not_visible(self, locator, time=10):
        try:
            WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))
            return True
        except:
            return False
