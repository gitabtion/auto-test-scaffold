from base.base_test_case import BaseUnitTestCase
from common import util
import unittest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


class TestCase(BaseUnitTestCase):
    def setUp(self):
        self.driver = util.get_driver()
        self.login = LoginPage(self.driver)

    def test_login(self):
        self.login.login('001', '1')
        self.assertEqual(self.driver.find_element(by=By.ID, value='userName').text, 'test_01', msg="没有找到")
        util.save_screenshot(self.driver, 'after_login.png')


if __name__ == '__main__':
    unittest.main()
