import requests
# import json
# import allure
import curl
from faker import Faker

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

# from data import Credential


# class ApiMethods:
    # def register_user(self):
    #     # Создаем пользователя
    #     faker = Faker()
    #     user_data = {
    #         "email": faker.email(),
    #         "password": "password",
    #         "name": "Test User"
    #     }
    #     response = requests.post(curl.REGISTER_API_URL, json=user_data)
    #     assert response.status_code != 403  # Проверка на существование пользователя
    #     yield response.json()
    #     # Удаление пользователя
    #     headers = {
    #         "Authorization": access_token
    #     }
    #     requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)

    # @staticmethod
    # def login(email, password):
    #     return requests.post(curl.LOGIN_API_URL, email, password)
        # return requests.post(curl.LOGIN_API_URL, json={"email": Credential.email, "password": Credential.password})



# import time
#
# class APIClient:
#     def __init__(self, base_url=curl.main_site):
#         self.base_url = base_url
#         self.headers = {'Content-Type': 'application/json'}
#
#     def _get_headers_with_token(self, token):+
#         """Вспомогательная функция для добавления токена в заголовок Authorization."""
#         headers = self.headers.copy()  # Создаем копию основных заголовков
#         if token:
#             headers['Authorization'] = f"{token}"
#         return headers
#
#     @allure.step("Регистрация пользователя")+
#     def register_user(self, email, password, name):
#         url = curl.register_api
#         payload = {"email": email, "password": password, "name": name}
#         response = requests.post(url, data=json.dumps(payload), headers=self.headers)
#         return response
#
#     @allure.step("Авторизация пользователя")
#     def login_user(self, email, password):
#         url = curl.login_api
#         payload = {"email": email, "password": password}
#         response = requests.post(url, data=json.dumps(payload), headers=self.headers)
#         return response
#
#     # @allure.step("Выход пользователя из системы")
#     # def logout_user(self, refresh_token):
#     #     url = curl.logout_api
#     #     payload = {"token": refresh_token}
#     #     response = requests.post(url, data=json.dumps(payload), headers=self.headers)
#     #     return response
#
#     @allure.step("Обновление токена")
#     def refresh_token(self, refresh_token):
#         url = curl.token_api
#         payload = {"token": refresh_token}
#         response = requests.post(url, data=json.dumps(payload), headers=self.headers)
#         return response
##
#     @allure.step("Создание заказа")
#     def create_order(self, ingredients, token=None):
#         url = curl.orders_api
#         payload = {"ingredients": ingredients}
#         headers = self._get_headers_with_token(token)  # Получаем заголовки с токеном
#         response = requests.post(url, data=json.dumps(payload), headers=headers)
#         return response
#
#     @allure.step("Удаление пользователя")
#     def delete_user(self, token):
#          print(f"Deleting user with token: {token}")  # Добавили print
#          url = curl.user_api
#          headers = self._get_headers_with_token(token)  # Добавляем токен в заголовок
#          response = requests.delete(url, headers=headers)
#          print(f"Delete user response status code: {response.status_code}, json: {response.json()}")  # Добавили print
#          time.sleep(0.1)
#          return response