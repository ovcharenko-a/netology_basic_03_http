"""Модуль, описывающий класс SuperHero"""
import requests
from goodlogger import main_log

class SuperHero:
    """
    Класс для получения данных о супергероях.
    """
    START_URL = 'https://superheroapi.com/api/'

    @main_log
    def __init__(self, name, set_api_key=""):
        self.api_key = set_api_key
        self.name = name
        self.intelligence = 0

    @main_log
    def load_iq(self, custom_api_key=""):
        """
        Получить данные об интеллекте с удаленного сервера.
        """
        if custom_api_key:
            api_key = custom_api_key
        elif self.api_key:
            api_key = self.api_key
        else:
            return "ошибка api ключа"
        response = requests.get(self.START_URL + api_key + "/search/" + self.name)
        if 200 <= response.status_code < 300:
            data = response.json()
            if data["response"] == "success":
                self.intelligence = int(data["results"][0]["powerstats"]["intelligence"])
            else:
                print(data["error"])
        else:
            print(f"Ошибка web-запроса, статус: {response.status_code}")