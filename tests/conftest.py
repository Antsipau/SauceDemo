import logging
import logging.config
import pytest
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def my_logger():
    logfile = 'test.log'
    log = logging.getLogger("my_log")
    log.setLevel(logging.INFO)
    FH = logging.FileHandler(logfile)
    basic_formater=logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
    FH.setFormatter(basic_formater)
    log.addHandler(FH)
    return log


@pytest.fixture(autouse=True)
def registration():
    """Registration fixture"""
    driver = webdriver.Chrome('/home/jrankel/SauceDemo/resources/chromedriver')
    driver.get('https://www.saucedemo.com/')
    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    driver.find_element(By.ID, "login-button").submit()

    driver.get('https://www.saucedemo.com/inventory.html')
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    yield driver
    driver.close()
