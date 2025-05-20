import allure
import pytest

from data import Constants


class TestCreateCourier:

    @allure.description('Создаем курьера. Проверяем код ответа')
    def test_create_courier(self, courier, courier_methods):
        status_code, json, _, _ = courier
        assert status_code == 201 and json == {'ok': True}, (
            f"Status is {status_code} and text is {json}"
        )

    @allure.description('Проверяем возможность создания двух одинаковых курьеров.')
    def test_create_twin_courier(self, courier, courier_methods):
        response = courier_methods.create_courier(Constants.DATA)
        assert response.status_code == 409 and response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.',(
            f'Status is {response.status_code}, message is {response.json()["message"]}'
        )

    @allure.description('Проверяем, что если одного из полей нет, запрос возвращает ошибку')
    @pytest.mark.parametrize('login_data', [{"login": "petro"}, {"password": "12345"}])
    def test_create_with_only_login_courier_code_400(self, courier_methods, login_data):
        response = courier_methods.create_courier(login_data)
        assert response.status_code == 400 and response.json()["message"] == 'Недостаточно данных для создания учетной записи'
