import requests


class SuperHero:
    START_URL = 'https://superheroapi.com/api/'

    def __init__(self, name, set_api_key="", hero_id=""):
        self.api_key = set_api_key
        self.name = name
        self.hero_id = hero_id
        self.intelligence = 0

    def load_id(self, custom_api_key=""):
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
                self.hero_id = data["results"][0]["id"]
                self.intelligence = int(data["results"][0]["powerstats"]["intelligence"])
            else:
                print(data["error"])
        else:
            print(f"Ошибка web-запроса, статус: {response.status_code}")