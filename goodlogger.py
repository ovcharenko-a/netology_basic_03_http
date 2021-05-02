"""
декоратор - логгер.
Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
"""
from datetime import datetime


def main_log(func):
    def wrapper_log(*args, **kwargs):
        _path = "main.log"
        _name = func.__name__
        _now = datetime.now()
        with open(_path, "a", encoding="UTF-8") as file_log:
            file_log.write(f'{_now} Функция {_name} с аргументами {args}, {kwargs} вернула ')
        _result = func(*args, **kwargs)
        with open(_path, "a") as file_log:
            file_log.write(f'{_result};\n')
        return _result

    return wrapper_log


def custom_log(_path="main.log"):
    def main_log(func):
        def wrapper_log(*args, **kwargs):
            _name = func.__name__
            _now = datetime.now()
            with open(_path, "a", encoding="UTF-8") as file_log:
                file_log.write(f'{_now} Функция {_name} с аргументами {args}, {kwargs} вернула ')
            _result = func(*args, **kwargs)
            with open(_path, "a") as file_log:
                file_log.write(f'{_result};\n')
            return _result
        return wrapper_log
    return main_log
