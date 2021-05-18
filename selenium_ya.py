import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import configparser


class YandexLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        config = configparser.ConfigParser()
        config.read("token.conf")
        self.login_ = config["selenium"]["yandex_login"]
        self.pass_ = config["selenium"]["yandex_pass"]

    def test_search_in_python_org(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get('https://passport.yandex.ru/profile')
        assert "Авторизация" in driver.title
        elem_log = driver.find_element_by_id("passp-field-login")
        elem_log.send_keys(self.login_)
        elem_log.send_keys(Keys.ENTER)
        elem_pass = driver.find_element_by_name("passwd")
        elem_pass.send_keys(self.pass_)
        elem_pass.send_keys(Keys.ENTER)
        assert "Управление аккаунтом" not in driver.page_source


    def tearDown(self):
        # self.driver.close()
        pass


if __name__ == "__main__":
    unittest.main()
