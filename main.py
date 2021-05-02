"""
Работа с библиотекой requests, http-запросы
"""
import configparser
from superhero import SuperHero
from yandexupload import YaUploader
from stackoverflowapi import StackOverflow
from datetime import datetime, timedelta
from goodlogger import main_log, custom_log


def start_task(func):
    def wrapper(*task):
        print(f"СТАРТ ЗАДАЧИ {func.__name__}")
        func()
        print(f"КОНЕЦ ЗАДАЧИ {func.__name__}")

    return wrapper


@start_task
@main_log
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
@main_log
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


@start_task
@custom_log("stack_log\\main.log")
def task_3():
    python_stack = StackOverflow()
    # Слишком много!
    set_time = datetime.today() - timedelta(1)
    my_tag = "python"
    input_temp = input("Результатов может быть много. Точно хотите продолжить? (y/n): ")
    if input_temp.lower() in ('yes', 'да', 'y', 'д'):
        result = python_stack.print_questions_of_tag(my_tag, set_time)
        if type(result) == list:
            print(f"Получено {len(result)} вопросов по теме {my_tag}")
        else:
            print(f"Ошибка! До возникновения ошибки получено {len(result)} вопросов по теме {my_tag}")


if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
