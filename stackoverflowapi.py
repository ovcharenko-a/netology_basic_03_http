import requests
from datetime import datetime
from goodlogger import custom_log

class StackOverflow:
    @custom_log("stack_log\\main.log")
    def __init__(self):
        pass

    @custom_log("stack_log\\main.log")
    def print_questions_of_tag(self, input_tag: str, from_date=""):
        url_api = "https://api.stackexchange.com/2.2/questions"
        params = {
            "order": "desc",
            "sort": "creation",
            "tagged": input_tag,
            "site": "stackoverflow",
            "pagesize": 100,
            "filter": "!--Fgzp2PZM*u"
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
                items = response.json()
                for item in items["items"]:
                    print(item["title"])
                    titles.append(item["title"])
            else:
                print("Ошибка запроса:")
                print(response.status_code)
                print(response.text)
                return titles
            if not response.json()["has_more"]:
                return titles
