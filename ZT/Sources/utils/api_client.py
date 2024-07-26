import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_users(self):
        response = requests.get(f"{self.base_url}/users")
        response.raise_for_status()
        return response.json()

    def get_user(self, user_id):
        response = requests.get(f"{self.base_url}/users/{user_id}")
        response.raise_for_status()
        return response.json()

    def create_user(self, user_data):
        response = requests.post(f"{self.base_url}/users", json=user_data)
        response.raise_for_status()
        return response.json()

    def update_user(self, user_id, user_data):
        response = requests.put(f"{self.base_url}/users/{user_id}", json=user_data)
        response.raise_for_status()
        return response.json()

    def delete_user(self, user_id):
        response = requests.delete(f"{self.base_url}/users/{user_id}")
        response.raise_for_status()
        return response.status_code
