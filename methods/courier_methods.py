import allure
import requests
from data import Constants


class CourierMethods:

    @allure.step('Метод удаления курьера')
    def delete_courier(self, id):
        response = requests.delete(f'{Constants.BASE_URL}{Constants.COURIERS_URL}{id}')
        return response

    @allure.step('Метод для входа курьера в систему')
    def login_courier(self, some_data):
        payload=some_data
        response = requests.post(f'{Constants.BASE_URL}{Constants.COURIERS_URL}login', data=payload)
        return response

    @allure.step('Метод создания курьера')
    def create_courier(self, some_data):
        payload= some_data
        response = requests.post(f'{Constants.BASE_URL}{Constants.COURIERS_URL}', data=payload)
        return response
