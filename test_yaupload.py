import configparser
import requests
import unittest
from parameterized import parameterized



class TestUpload(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config = configparser.ConfigParser()  # создаём объекта парсера
        config.read("token.conf")
        cls.API = config["main"]["yandex_token"]
        cls.host = "https://cloud-api.yandex.net/v1/disk/resources"
        cls.headers = {
            "Authorization": "OAuth " + cls.API,
            "User-Agent": "netology-test",
            # "Content - Type": "application/json",
        }

    @classmethod
    def tearDownClass(cls):
        params = {
            "path": '/testnetologyemptydir/'
        }
        response = requests.request('DELETE', cls.host, params=params, headers=cls.headers)

    @parameterized.expand([['correct_upload', '/testnetologyemptydir/', 201],
                           ['double_upload', '/testnetologyemptydir/', 409],
                           ['incorrect_upload', '/testnetologyemptydir/1/2', 409]])
    def test_upload(self, name_, path, assert_status):
        params = {
            "path": path
        }
        response = requests.request('PUT', self.host, params=params, headers=self.headers,)
        self.assertEqual(assert_status, response.status_code,)

if __name__ == '__main__':
    unittest.main()
