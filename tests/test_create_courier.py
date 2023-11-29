import allure
import pytest
import requests

import helpers
from endpoints import EndpointsUrl


@allure.suite('Создание курьера')
class TestCreateCourier:

    @allure.title('Успешное создания курьера')
    @allure.description('Запрос проверяет, что курьер создан со всеми обязательными полями')
    def test_create_courier_success(self, unregistered_courier):
        payload = unregistered_courier
        with allure.step('Отправляем запрос'):
            response = requests.post(EndpointsUrl.CREATE_COURIER, data=payload)
        with allure.step('Проверяем код ответа и тело ответа'):
            assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Успешная проверка создания курьера')
    @allure.description('Запрос проверяет, что курьер создается без поля "firstName"')
    def test_create_courier_without_firstname_success(self, unregistered_courier):
        payload = unregistered_courier
        payload['firstName'] = None
        response = requests.post(EndpointsUrl.CREATE_COURIER, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Ошибка при создании одинаковых курьеров')
    @allure.description('Проверяем ошибку при создании курьера с уже существующими данными')
    def test_create_same_courier(self, unregistered_courier):
        payload = unregistered_courier
        requests.post(EndpointsUrl.CREATE_COURIER, data=payload)
        response = requests.post(EndpointsUrl.CREATE_COURIER, data=payload)
        assert response.status_code == 409 and response.json().get('message') \
               == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Ошибка при создании курьера без обязательного поля')
    @allure.description('Проверяем ошибку создания курьера при отсутствии одного из обязательных полей')
    @pytest.mark.parametrize('deleted_field', ['login', 'password'])
    def test_create_courier_with_empty_field(self, deleted_field):
        login, password, first_name = helpers.generate_unregistered_courier()
        payload = {
            'login': login,
            'password': password,
            'firstName': first_name
        }
        del payload[deleted_field]
        response = requests.post(EndpointsUrl.CREATE_COURIER, data=payload)
        assert response.status_code == 400 and response.json().get('message')\
               == "Недостаточно данных для создания учетной записи"
