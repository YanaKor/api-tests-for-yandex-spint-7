import allure
import requests

from endpoints import EndpointsUrl


@allure.suite('Список заказов')
class TestOrderList:
    @allure.title('Проверка полного списка заказов')
    @allure.description('Проверка успешного возврата списка заказов в тело ответа')
    def test_oder_list(self):
        response = requests.get(EndpointsUrl.ORDER)
        assert response.status_code == 200 and 'orders' in response.json()
        assert type(response.json()['orders']) is list
