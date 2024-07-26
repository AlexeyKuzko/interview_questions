import pytest
import allure
from requests.exceptions import HTTPError
import random


@allure.feature('API')
def test_get_users(test_data):
    try:
        with allure.step("Fetch users from API"):
            users = test_data.api_client.get_users()
        with allure.step("Verify the response"):
            assert len(users) > 0, "No users found"
    except HTTPError as e:
        pytest.fail(f"HTTPError occurred: {e}")


@allure.feature('API')
def test_create_user(test_data):
    try:
        with allure.step("Create a new user"):
            user = test_data.create_test_user()
        with allure.step("Verify the user was created"):
            assert user["id"] is not None, "User ID should not be None"
        with allure.step("Clean up - delete the created user"):
            response_code = test_data.delete_test_user(user["id"])
            assert response_code == 200, "Failed to delete the user"
    except HTTPError as e:
        pytest.fail(f"HTTPError occurred: {e}")


@allure.feature('API')
def test_update_user(test_data):
    try:
        with allure.step("Fetch users from API"):
            users = test_data.api_client.get_users()
            user_id = random.choice([user["id"] for user in users if 1 <= user["id"] <= 10])

        with allure.step("Fetch user data for update test"):
            user = test_data.api_client.get_user(user_id)

        with allure.step("Update the user data"):
            updated_data = user.copy()
            updated_data["name"] = "Updated Test User"
            updated_user = test_data.api_client.update_user(user_id, updated_data)

        with allure.step("Verify the user was updated"):
            assert updated_user["name"] == "Updated Test User", "User name was not updated"
    except HTTPError as e:
        pytest.fail(f"HTTPError occurred: {e}")


@allure.feature('API')
def test_delete_user(test_data):
    try:
        with allure.step("Create a new user for delete test"):
            user = test_data.create_test_user()
        with allure.step("Delete the user"):
            response_code = test_data.delete_test_user(user["id"])
        with allure.step("Verify the user was deleted"):
            assert response_code == 200, "Failed to delete the user"
        with allure.step("Verify the user no longer exists"):
            with pytest.raises(HTTPError):
                test_data.api_client.get_user(user["id"])
    except HTTPError as e:
        pytest.fail(f"HTTPError occurred: {e}")