from faker.generator import random

from utils.api_client import APIClient


class Drivers:
    browsers = ["chrome", "firefox"]
    additional_browsers = ["edge", "safari", "opera"]  # далее можно поддержать эти браузеры


class Urls:
    base_url = "https://passport.yandex.ru",
    api_url = "https://jsonplaceholder.typicode.com"


class Paths:
    results_file = "results/test_results.txt"


class TestData:
    def __init__(self):
        self.api_client = APIClient(Urls.api_url)
        self.data = self.api_client.get_users()

    def num_of_failed_login_attempts(self):
        this_must_be_constaint =random.randint(1, 10) # но, по условиям задания, не должно быть хардкод значений
        return this_must_be_constaint

    def get_user(self, index):
        return self.data[index]

    def create_test_user(self):
        user_data = {
            "name": "Test User",
            "username": "testuser",
            "email": "testuser@example.com",
            "address": {
                "street": "Test Street",
                "suite": "Apt. 123",
                "city": "Test City",
                "zipcode": "12345",
            },
            "phone": "123-456-7890",
            "website": "testuser.com",
            "company": {
                "name": "Test Company",
                "catchPhrase": "Test Phrase",
                "bs": "test bs"
            }
        }
        return self.api_client.create_user(user_data)

    def delete_test_user(self, user_id):
        return self.api_client.delete_user(user_id)
