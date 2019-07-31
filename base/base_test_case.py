from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import datetime
from common.config import BASE_PATH
import unittest


class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    # 等待元素可见
    def wait_ele_visible(self, addr, by=By.XPATH, model='model.png', wait=30, requence=0.5):
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait, requence).until(EC.visibility_of_element_located((by, addr)))
            end = datetime.datetime.now()
            wait_time = (end - start).seconds
            # todo logging
        except:
            screen_pathname = os.path.join(BASE_PATH, 'logs', model)
            self.save_screen(screen_pathname)
            # print("元素不可见")
            raise

        pass

    def find_element(self, addr, by=By.XPATH):
        try:
            return self.driver.find_element(by=by, value=addr)
        except BaseException as e:
            print('error>>:', e)
            screen_pathname = os.path.join(BASE_PATH, 'logs', 'notfind.png')
            self.save_screen(screen_pathname)  # 截图
            raise  # 一旦执行了raise语句，raise后面的语句将不能执行。

    def find_elements(self, addr, by=By.XPATH):
        try:
            return self.driver.find_elements(by=by, value=addr)
        except BaseException as e:
            print('error>>:', e)
            screen_pathname = os.path.join(BASE_PATH, 'logs', 'notfind.png')
            self.save_screen(screen_pathname)
            raise

    def click(self, addr, by=By.XPATH):
        ele = self.find_element(addr, by=by)
        try:
            ele.click()
        except BaseException as e:
            print('error>>:', e)
            screen_pathname = os.path.join(BASE_PATH, 'logs', 'clickfailed.png')
            self.save_screen(screen_pathname)
            raise

    def input(self, addr, text, by=By.XPATH):

        ele = self.find_element(addr, by=by)
        try:
            ele.send_keys(text)
        except BaseException as e:
            print('error>>:', e)
            screen_pathname = os.path.join(BASE_PATH, 'logs', 'inputfailed.png')
            self.save_screen(screen_pathname)
            raise

    # def load_deafult_page(self):
    #
    #     self.get_switch_instance().default_content()

    def get_switch_instance(self):

        return self.driver.switch_to

    # 切入iframe
    def switch_iframe(self, value):
        """
            element = driver.switch_to.active_element
            alert = driver.switch_to.alert
            driver.switch_to.default_content()
            driver.switch_to.frame('frame_name')
            driver.switch_to.frame(1)
            driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
            driver.switch_to.parent_frame()
            driver.switch_to.window('main')

        :param value:
        :param logname:
        :return:
        """
        try:
            # self.driver.switch_to.frame(value)
            self.get_switch_instance().frame(value)
        except BaseException as e:
            print('errpr>>:', e)
            screen_pathname = os.path.join(BASE_PATH, 'logs', 'switchfailed.png')
            self.save_screen(screen_pathname)
            raise

    def save_screen(self, screen_name='screens.png'):
        screen_pathname = os.path.join(BASE_PATH, 'logs', screen_name)
        self.driver.save_screenshot(screen_pathname)


class DefaultBase(BasePage):

    def load_to_default(self):
        return self.get_switch_instance().default_content()


class BaseUnitTestCase(unittest.TestCase):

    def DiyassertEqual(self, expected_value, indentified, by=By.XPATH, msg=None):
        value = self.driver.find_element(by=by, value=indentified).text
        self.assertEqual(expected_value, value, msg=msg)

    def DiyassertIn(self, member, indentfy_list, by=By.XPATH, msg=None):
        value_list = self.driver.find_elements(by=by, value_list=indentfy_list)
