BASE_URL = "https://stellarburgers.nomoreparties.site/" # главная, конструктор
LOGIN_URL = BASE_URL + "login"  # ЛК для forgot_password_page, login_page
FORGOT_PASSWORD_URL = BASE_URL +"forgot-password" # забыл пароль
RESET_PASSWORD_URL = BASE_URL + "reset-password" # восстановить пароль
REGISTER_URL = BASE_URL + "register"

CONSTRUCTOR_URL = BASE_URL
FEED_URL = BASE_URL + "feed" # Лента заказов
INGREDIENT_DETAILS_URL = BASE_URL + "ingredient/" # добавить ингредиенты

PROFILE_URL = BASE_URL + "account/profile"    # Профиль
ORDER_HISTORY_URL = BASE_URL + "account/order-history" # история заказов

# API endpoints
REGISTER_API_URL = BASE_URL + "api/auth/register"
LOGIN_API_URL = BASE_URL + "api/auth/login"
ORDERS_API_URL = BASE_URL + "api/orders" # Needs authentication
