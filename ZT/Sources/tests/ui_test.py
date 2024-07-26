import pytest
import allure
from data import *

@allure.feature('Проверка успешной авторизации с правильными credentials')
@pytest.mark.usefixtures("init_driver")
def test_successful_login(base_page, test_data):
    user = test_data.get_user(0)
    username = user["email"]
    password = user["website"]

    with allure.step("Load login page"):
        base_page.load()

    with allure.step("Enter username and password"):
        base_page.login(username, password)

    with allure.step("Verify successful login"):
        assert "expected element after login" in base_page.get_page_source()

@allure.feature('Проверка ошибки при вводе неверного пароля')
@pytest.mark.usefixtures("init_driver")
def test_failed_login_invalid_password(base_page, test_data):
    user = test_data.get_user(0)
    username = user["email"]
    invalid_password = "invalid_password"

    with allure.step("Load login page"):
        base_page.load()

    with allure.step("Enter username and invalid password"):
        base_page.login(username, invalid_password)

    with allure.step("Verify error message"):
        assert "Неверный пароль" in base_page.get_error_message()

@allure.feature('Проверка ошибки при вводе неверного логина')
@pytest.mark.usefixtures("init_driver")
def test_failed_login_invalid_username(base_page):
    invalid_username = "invalid_username"
    password = "password"

    with allure.step("Load login page"):
        base_page.load()

    with allure.step("Enter invalid username and password"):
        base_page.login(invalid_username, password)

    with allure.step("Verify error message"):
        assert "Такого аккаунта нет" in base_page.get_error_message()

@allure.feature('Проверка возможности восстановления пароля')
@pytest.mark.usefixtures("init_driver")
def test_password_recovery(base_page):
    with allure.step("Load login page"):
        base_page.load()

    with allure.step("Click password recovery link"):
        base_page.click_password_recovery()
    # далее следует добавить реальные шаги для восстановления пароля, но мне мешают капчи Яндекса

@allure.feature('Проверка блокировки УЗ после n неудачных попыток входа')
@pytest.mark.usefixtures("init_driver")
def test_account_lockout_after_failed_attempts(base_page, test_data):
    user = test_data.get_user(0)
    username = user["email"]
    invalid_password = "invalid_password"

    with allure.step("Load login page"):
        base_page.load()

    for _ in range(TestData.num_of_failed_login_attempts):
        with allure.step("Attempt to login with invalid password"):
            base_page.login(username, invalid_password)
            base_page.load()

    with allure.step("Verify account lockout"):
        assert "expected lockout message" in base_page.get_page_source()