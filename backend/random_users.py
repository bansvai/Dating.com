import requests

class RandomUsers:
    @staticmethod
    def generate_users(num_users):
        response = requests.get(f"https://randomuser.me/api/?results={num_users}")
        if response.status_code == 200:
            return response.json()["results"]
        else:
            error_message = f"Failed to fetch users from randomuser.me API: {response.status_code} - {response.text}"
            raise Exception(error_message)