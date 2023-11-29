import allure
import requests

import helpers
from endpoints import EndpointsUrl


@allure.suite('Удаление курьера')
class TestDeleteCourier:
    @allure.title('Успешное удаление курьера')
    @allure.description('Проверка удаления курьера со существующим id')
    def test_delete_courier_success(self):
        courier = helpers.new_courier()
        resp = requests.post(EndpointsUrl.LOGIN, data=courier)
        courier_id = resp.json()["id"]
        payload = {"id": courier_id}
        response = requests.delete(EndpointsUrl.COURIER + '/' + str(courier_id), data=payload)

        assert response.status_code == 200 and response.text == '{"ok":true}'

    @allure.title('Ошибка при удалении курьера')
    @allure.description('Проверка удаления курьера с несуществующим id')
    def test_delete_courier_with_fake_id(self):
        courier_id = helpers.non_existing_courier()
        payload = {"id": courier_id}
        response = requests.delete(EndpointsUrl.COURIER + '/' + str(courier_id), data=payload)

        assert response.status_code == 404 and response.json().get('message') == "Курьера с таким id нет."






