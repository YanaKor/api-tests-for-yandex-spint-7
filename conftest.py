import pytest
import requests

from endpoints import EndpointsUrl
import helpers


@pytest.fixture
def unregistered_courier():
    login, password, first_name = helpers.generate_unregistered_courier()
    payload = {
        'login': login,
        'password': password,
        'firstName': first_name
    }

    yield payload

    del payload['firstName']
    response = requests.post(EndpointsUrl.LOGIN_COURIER, data=payload)
    courier_id = response.json()["id"]
    requests.delete(f'{EndpointsUrl.CREATE_COURIER}{courier_id}')


@pytest.fixture
def registered_courier():
    login, password, first_name = helpers.register_new_courier_and_return_login_password()
    payload = {
        'login': login,
        'password': password
    }

    yield payload

    response = requests.post(EndpointsUrl.LOGIN_COURIER, data=payload)
    courier_id = response.json()["id"]
    requests.delete(f'{EndpointsUrl.CREATE_COURIER}{courier_id}')