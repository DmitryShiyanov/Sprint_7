import allure
import pytest

from data import Constants


class TestCreateOrder:

    @allure.description('Проверка создания заказа')
    def test_create_order(self, courier, order_methods):
        status_code, json = order_methods.create_order(Constants.ORDER_1)
        assert status_code == 201 and 'track' in json, (
            f'Status is {status_code} and json is {json}'
        )

    @allure.description('Создание заказа с разными условиями')
    @pytest.mark.parametrize(
        'order_params',
        [   Constants.ORDER_1,
            Constants.ORDER_2,
            Constants.ORDER_3
        ]
    )
    def test_check_order_create_differ_color_id(self, courier, order_methods, order_params):
        status_code, json = order_methods.create_order(order_params)
        assert status_code == 201, (
            f'Status is {status_code}'
        )

    @allure.description('Проверка списка заказов по ID курьера ')
    def test_get_orders_courier(self, courier, order_methods):
        status_code, json = order_methods.get_orders(courier[3])
        assert status_code == 200 and 'orders' in json, (
            f'Status is {status_code} and json is {json}'
        )