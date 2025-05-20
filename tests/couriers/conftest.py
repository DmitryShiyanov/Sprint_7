import pytest

from data import Constants
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods

@pytest.fixture
def courier_methods():
    return CourierMethods()

@pytest.fixture
def order_methods():
    return OrderMethods()

@pytest.fixture
def courier():
    response = CourierMethods().create_courier(Constants.DATA)
    resp = CourierMethods().login_courier(Constants.DATA)
    yield response.status_code, response.json(), resp, resp.json()["id"]
    CourierMethods().delete_courier(resp.json()["id"])
