import allure
import requests
import pytest

from endpoints import EndpointsUrl


@allure.suite('Создание заказа')
class TestCreateOrder:
    @allure.title('Проверка создания заказа')
    @allure.description('Параметризированный тест по созданию заказа с разными цветами и без него')
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])
    def test_create_order(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }
        response = requests.post(EndpointsUrl.ORDER, json=payload)
        assert response.status_code == 201 and 'track' in response.text
