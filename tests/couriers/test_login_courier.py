import allure
import pytest


class TestLoginCourier:

    @allure.description('Проверяем авторизацию. Запрос возвращает ID курьера')
    def test_login_courier(self, courier, courier_methods):
        status_code, json, resp, _ = courier
        assert resp.status_code == 200 and 'id' in resp.json(), (
            f'Status is {resp.status_code} and json {resp.json()}'
        )

    @allure.description('Проверяем возможность логина без одного обязательного поля')
    @pytest.mark.parametrize("pay_load_params", [{"password": "12345"}])
    def test_courier_login_without_log_pass_status_code_400(self, courier, courier_methods, pay_load_params):
        response = courier_methods.login_courier(pay_load_params)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа",(
                f'Status is {response.status_code}, message is {response.json()["message"]}'
        )

    @allure.description('Тест авторизации под несуществующими данными пользователя')
    def test_incorrect_user_status_code_404(self, courier_methods):
        user_data = {
            "login": "abbr",
            "password": "12345"
        }
        response = courier_methods.login_courier(user_data)
        assert response.json()["message"] == 'Учетная запись не найдена' and response.status_code == 404
