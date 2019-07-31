from base.base_test_case import BasePage
from common.config import BASE_URL
from time import sleep
import os
from selenium.webdriver.common.by import By
from common.config import BASE_PATH


class LoginPage(BasePage):
    url = 'login/login.html'
    username = 'username'
    password = 'password'
    login_btn = 'loginBtn'

    def login(self, user='001', pwd='1'):
        self.driver.get(BASE_URL + self.url)

        screen_name = os.path.join(BASE_PATH, 'logs', 'login_page.png')
        self.wait_ele_visible(self.username, by=By.ID, model=screen_name)

        self.input(self.username, user, by=By.ID)
        self.input(self.password, pwd, by=By.ID)
        self.click(self.login_btn, by=By.ID)
        sleep(3)
