from json import JSONDecodeError

import allure
import requests
from data import Constants


class OrderMethods():

    @allure.step('Метод создания заказа')
    def create_order(self, params):
        response = requests.post(f'{Constants.BASE_URL}{Constants.ORDERS_URL}', json=params)
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

    @allure.step('Метод получения списка заказов по ID')
    def get_orders(self, id):
        response = requests.get(f'{Constants.BASE_URL}{Constants.ORDERS_URL}?courierId={id}')
        return response.status_code, response.json()
