
import requests
import pytest
from selenium import webdriver
from Diplom_3.curl import BASE_URL, REGISTER_API_URL, LOGIN_API_URL, ORDERS_API_URL
import allure
from faker import Faker


# подключаем 2 браузера
@pytest.fixture(params=['firefox','chrome'])
def driver(request):
    driver = None
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    driver.implicitly_wait(10)  # Неявное ожидание (ждать до 10 секунд, пока элемент появится)

    yield driver
    driver.quit()

# работа с API
# фикстура для создания пользователя
@pytest.fixture()
def user_setup():

    # Создаем пользователя
    faker = Faker()
    user_data = {
        "email": faker.email(),
        "password": "password",
        "name": "Test User"
    }

    response = requests.post(REGISTER_API_URL, json=user_data)
    assert response.status_code != 403, "Такой пользователь уже существует"  # Проверка на существование пользователя

    user_data_login = {
        "email": user_data["email"],
        "password": "password"
    }

    return user_data_login

# Фикстура для авторизации
@pytest.fixture(scope='function')
def upload_token_to_session(driver, user_setup):
    token_response = requests.post(LOGIN_API_URL, user_setup).json()
    driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", 'accessToken',
                          token_response['accessToken'])
    driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", 'refreshToken',
                          token_response['refreshToken'])
    yield token_response['accessToken']
    # Удаление пользователя
    headers = {"Authorization": token_response['accessToken']}
    #       print("Отправка запроса на удаление пользователя")
    respon = requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)
