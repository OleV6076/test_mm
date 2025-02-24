import requests

class ReqresAPI:
    BASE_URL = "https://reqres.in/api"

    def __init__(self):
        self.session = requests.Session()

    def get_users(self, page=1):
        # Получение списка пользователей
        response = self.session.get(f"{self.BASE_URL}/users", params={"page": page})
        return response

    def create_user(self, name, job):
        # Создание нового пользователя
        payload = {"name": name, "job": job}
        response = self.session.post(f"{self.BASE_URL}/users", json=payload)
        return response

    def update_user(self, user_id, name, job):
        # Обновление данных пользователя
        payload = {"name": name, "job": job}
        response = self.session.put(f"{self.BASE_URL}/users/{user_id}", json=payload)
        return response

    def delete_user(self, user_id):
        # Удаление пользователя
        response = self.session.delete(f"{self.BASE_URL}/users/{user_id}")
        return response