import requests
from datetime import datetime


class StackOverflow:
    def __init__(self):
        pass

    def get_questions_of_tag(self, input_tag: str, from_date=""):
        url_api = "https://api.stackexchange.com/2.2/questions"
        params = {
            "order": "desc",
            "sort": "activity",
            "tagged": input_tag,
            "site": "stackoverflow",
            "filter": "!0j_J2CikNeRO"
        }
        if from_date:
            if type(from_date) == datetime:
                params["fromdate"] = from_date.toordinal()
            if type(from_date) == int or type(from_date) == str:
                params["fromdate"] = from_date
        titles = []
        page = 0
        while True:
            page += 1
            params["page"] = page
            response = requests.get(url_api, params=params)
            if response.status_code == 200:
                for item in response.json()["items"]:
                    titles.append(item["title"])
            else:
                return "Ошибка запроса"
            if not response.json()["has_more"]:
                return titles
