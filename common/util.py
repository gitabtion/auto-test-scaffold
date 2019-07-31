import os
from common.config import BASE_PATH
from selenium import webdriver
from common.config import DRIVER_DIR
from time import sleep


def get_driver():
    driver = webdriver.Chrome(executable_path=DRIVER_DIR)
    driver.maximize_window()
    return driver


def save_screenshot(driver, name):
    sleep(3)
    name = os.path.join(BASE_PATH, 'logs', name)
    driver.get_screenshot_as_file(name)
