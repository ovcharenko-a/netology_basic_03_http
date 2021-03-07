"""
Работа с библиотекой requests, http-запросы
"""
import configparser
from superhero import SuperHero
from yandexupload import YaUploader

def start_task(func):
    def wrapper():
        print(f"СТАРТ ЗАДАЧИ {func.__name__}")
        func()
        print(f"КОНЕЦ ЗАДАЧИ {func.__name__}")

    return wrapper


@start_task
def task_1():
    """
    Определим, кто самый умный супергерой
    """
    API = "2619421814940190"
    hulk = SuperHero("Hulk", API)
    captain_america = SuperHero("Captain America", API)
    thanos = SuperHero("Thanos", API)
    heroes = [hulk, captain_america, thanos]
    for hero in heroes:
        hero.load_iq()
    heroes_iq = {hero.intelligence: hero for hero in heroes}
    key = max(heroes_iq.keys())
    print(f"Умнейший из героев {heroes_iq[key].name}, с интеллектом {heroes_iq[key].intelligence}")

@start_task
def task_2():
    """
    Загрузка файла на сервер
    """
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("token.conf")
    API = config["main"]["yandex_token"]
    uploader = YaUploader(API)
    result = uploader.upload("helloworld.txt")
    print(result)


if __name__ == "__main__":
    task_1()
    task_2()
