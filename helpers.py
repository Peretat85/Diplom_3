import pytest
import secrets
import string
from faker import Faker

def generate_user_data(name_prefix="Test User"):
    """Генерирует случайные данные пользователя."""
    faker = Faker()
    email = faker.email()
    password = ''.join(secrets.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    name = f"{name_prefix} {secrets.randbelow(100)}" # Добавляем случайное число
    return {"email": email, "password": password, "name": name}

@pytest.fixture(scope="function")
def new_user_data():
    """Фикстура для создания случайных данных пользователя."""
    return generate_user_data()

@pytest.fixture(scope="function")
def new_user_data_2():
    """Фикстура для создания случайных данных второго пользователя."""
    return generate_user_data(name_prefix="Second User")