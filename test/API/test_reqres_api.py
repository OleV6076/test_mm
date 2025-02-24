import pytest
from API.reqres_api import ReqresAPI
import allure

@pytest.fixture(scope="module")
def api_client():
    # Инициализация клиента API
    client = ReqresAPI()
    yield client

@allure.feature("Reqres API")
@allure.story("Получение списка пользователей")
def test_get_users(api_client):
    with allure.step("Отправка запроса на получение списка пользователей"):
        response = api_client.get_users(page=1)

    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"

    with allure.step("Проверка наличия данных о пользователях"):
        data = response.json()
        assert "data" in data, "Отсутствует поле 'data' в ответе"
        assert len(data["data"]) > 0, "Список пользователей пуст"

@allure.feature("Reqres API")
@allure.story("Создание нового пользователя")
def test_create_user(api_client):
    name = "Oleg"
    job = "AQA"

    with allure.step(f"Отправка запроса на создание пользователя с именем {name} и должностью {job}"):
        response = api_client.create_user(name=name, job=job)

    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 201, f"Ожидался код 201, но получен {response.status_code}"

    with allure.step("Проверка корректности созданного пользователя"):
        data = response.json()
        assert data["name"] == name, f"Имя не соответствует ожидаемому: {name}"
        assert data["job"] == job, f"Должность не соответствует ожидаемой: {job}"

@allure.feature("Reqres API")
@allure.story("Обновление данных пользователя")
def test_update_user(api_client):
    user_id = 2
    new_name = "John Doe"
    new_job = "Developer"

    with allure.step(f"Отправка запроса на обновление данных пользователя с ID={user_id}"):
        response = api_client.update_user(user_id=user_id, name=new_name, job=new_job)

    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"

    with allure.step("Проверка корректности обновленных данных"):
        data = response.json()
        assert data["name"] == new_name, f"Имя не соответствует ожидаемому: {new_name}"
        assert data["job"] == new_job, f"Должность не соответствует ожидаемой: {new_job}"

@allure.feature("Reqres API")
@allure.story("Удаление пользователя")
def test_delete_user(api_client):
    user_id = 2

    with allure.step(f"Отправка запроса на удаление пользователя с ID={user_id}"):
        response = api_client.delete_user(user_id=user_id)

    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 204, f"Ожидался код 204, но получен {response.status_code}"