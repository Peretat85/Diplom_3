from selenium.webdriver.common.by import By

# главная страница
class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[./p[text()='Конструктор']]")
    FEED_BUTTON = (By.XPATH, "//a[./p[text()='Лента Заказов']]")
    INGREDIENT_BUN = (By.XPATH, "//ul[contains(@class, 'BurgerIngredients_ingredients')]/a[1]/img")
    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    INGREDIENT_MODAL_HEADER = (By.XPATH, "//div[contains(@class, 'Modal_modal')]/div/h2[text()='Детали ингредиента']")
    INGREDIENT_MODAL_CLOSE_BUTTON = (By.XPATH, "//div/section[1]/div[1]/button")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # New
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")  # New
    ORDER_ID_TEXT = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//p[text()='идентификатор заказа']")  # New
    ORDER_INGREDIENT = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket')]")
    INGREDIENT_COUNTER = (By.XPATH, "//ul[contains(@class, 'BurgerIngredients_ingredients')]/a[1]/div/p") # заменить

# страница входа https://stellarburgers.nomoreparties.site/login
class LoginPageLocators:
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']") # дубль от Профиля, чтобы работал переход

# страница восстановления пароля с кодом из письма https://stellarburgers.nomoreparties.site/reset-password
class ForgotPasswordPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    RESET_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div/*[@viewBox='0 0 24 24']")
    PASSWORD_FIELD = (By.XPATH, "//div/label[text()='Пароль']")

# страница восстановления https://stellarburgers.nomoreparties.site/reset-password
class ResetPasswordPageLocators:
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']") # поле пароля
    PASSWORD_INPUT_ACTIVE = (By.XPATH, "//div[@class  = 'input pr-6 pl-6 input_type_password input_size_default']") #input_status_active
    ACTIV_CLASS = 'input_status_active' # заменить см ниже в локаторах и отправить в тест восстановления пароля
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div/*[@viewBox='0 0 24 24']")  # глазик
    PASSWORD_INPUT_FIELDSET = (By.XPATH, "//input[@type='text']") # код из письма
    BUTTON_SAVE = (By.XPATH, "//button[text()='Сохранить']")

# страница профиля https://stellarburgers.nomoreparties.site/profile
class ProfilePageLocators:  # New locators
    PERSONAL_CABINET_BUTTON = (By.XPATH, ".//p[contains(text(),'Личный Кабинет')]")
    ORDER_PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

# страница История заказов ЛК https://stellarburgers.nomoreparties.site/account/order-history
class FeedPageLocators: # локаторы
    PERSONAL_CABINET_BUTTON = (By.XPATH, ".//p[contains(text(),'Личный Кабинет')]")
    ORDER_ITEM = (By.XPATH, "//ul/li[1]//p[@class='text text_type_digits-default']") # первый заказ
    ORDER_DETAILS_MODAL = (By.XPATH,"//div[contains(@class, 'Modal_modal')]")
    ORDER_COMPOSITION_TEXT = (By.XPATH, "//p[text()='Cостав']") #//p[@class='text text_type_main-medium mb-8']

    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    ORDER_IN_FEED_ORDERS = (By.XPATH, "//li//p[@class='text text_type_digits-default']")
    ALL_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::*")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::*")

    IN_PROGRESS_ORDERS = (By.XPATH, "//h2[text() = 'В работе']/following-sibling::div/ul")
    IN_PROGRESS_ORDER_ID = (By.XPATH, "//div[1]/ul[2]/li[1]")

# упрощение локаторов
class Locators:
    login_page = LoginPageLocators()
    forgot_password_page = ForgotPasswordPageLocators()
    reset_password_page = ResetPasswordPageLocators()
    profile_page = ProfilePageLocators()
    main_page = MainPageLocators()
    feed_page = FeedPageLocators()
    EMAIL = "test@example.com"
    ACTIVE_CLASS = "input__placeholder-focused"

    # надписи "булки"
    inscription_bread = (By.XPATH, ".//span[contains(text(),'Булки')]")

    # кнопка_надпись "Личный кабинет"
    PERSONAL_CABINET_BUTTON = (By.XPATH, ".//p[contains(text(),'Личный Кабинет')]")
    



