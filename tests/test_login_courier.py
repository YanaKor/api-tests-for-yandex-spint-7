import pytest
import requests
import allure

import helpers
from endpoints import EndpointsUrl


@allure.suite('Логин курьера')
class TestLoginCourier:

    @allure.title('Успешная авторизация курьера')
    @allure.description('Проверка "id" курьера при авторизации')
    def test_login_courier_success(self, registered_courier):
        payload = registered_courier
        response = requests.post(EndpointsUrl.LOGIN, data=payload)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Ошибка авторизации курьера')
    @allure.description('Проверка входа без заполненного обязательного поля')
    @pytest.mark.parametrize('field_to_change', ['login', 'password'])
    def test_login_courier_without_password_field(self, registered_courier, field_to_change):
        payload = registered_courier.copy()
        payload[field_to_change] = ''
        response = requests.post(EndpointsUrl.LOGIN, data=payload)
        assert response.status_code == 400 and response.json().get('message') \
               == "Недостаточно данных для входа"

    @allure.title('Ошибка авторизации курьера')
    @allure.description('Проверка авторизации курьера с невалидными данными')
    @pytest.mark.parametrize('invalid_field', ['login', 'password'])
    def test_login_courier_with_invalid_field(self, registered_courier, invalid_field):
        payload = registered_courier.copy()
        payload[invalid_field] += '1'
        response = requests.post(EndpointsUrl.LOGIN, data=payload)
        assert response.status_code == 404 and response.json().get('message') == "Учетная запись не найдена"

    @allure.title('Ошибка авторизации')
    @allure.description('Проверка авторизации несущетвующего курьера')
    def test_login_unregistered_courier(self):
        login, password, first_name = helpers.generate_unregistered_courier()
        payload = {
            'login': login,
            'password': password
        }
        response = requests.post(EndpointsUrl.LOGIN, data=payload)
        assert response.status_code == 404 and response.json().get('message') == 'Учетная запись не найдена'



