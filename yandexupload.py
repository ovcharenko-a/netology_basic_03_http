"""Модуль описывающий класс YaUploader"""
import requests
from pathlib import Path
from goodlogger import main_log


class YaUploader:
    """
    Класс, реализующий загрузку файла на Яндекс диск.
    """
    HOST = "https://cloud-api.yandex.net:443"
    RESULT_KEY = {
        200: "Успех",
        201: "Файл был загружен без ошибок.",
        202: "Accepted — файл принят сервером, но еще не был перенесен непосредственно в Яндекс.Диск.",
        412: "Precondition Failed — при дозагрузке файла был передан неверный диапазон в заголовке Content-Range.",
        413: "Payload Too Large — размер файла превышает 10 ГБ.",
        500: "Internal Server Error или 503 Service Unavailable — ошибка сервера, попробуйте повторить загрузку.",
        507: "Insufficient Storage — для загрузки файла не хватает места на Диске пользователя."
    }

    @main_log
    def __init__(self, token: str):
        self.token = token

    @main_log
    def upload(self, input_file_path: str, remote_file_path: str = "", overwrite: bool = True):
        """Метод загруджает файл file_path на яндекс диск"""
        if not remote_file_path:
            remote_file_path = Path(input_file_path).name
        host_get = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            "Authorization": "OAuth " + self.token,
            "User-Agent": "netology-student",
            "Content - Type": "application/json",
        }
        params = {
            "path": remote_file_path,
            "overwrite": overwrite
        }
        preload_response = requests.get(host_get, params=params, headers=headers)
        upload_href = preload_response.json().get("href", None)
        if upload_href:
            try:
                with open(input_file_path, "rb") as file_head:
                    response_upload = requests.put(upload_href, data=file_head)
            except FileNotFoundError:
                return f"ошибка чтения файла {input_file_path}"
            return self.RESULT_KEY[response_upload.status_code]
        else:
            return (preload_response.json()["message"])




