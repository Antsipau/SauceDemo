import pickle
from selenium.webdriver.common.by import By


def test_find_elements_on_page(registration, my_logger):
    """Find all elements the web page"""
    driver = registration
    driver.get('https://www.saucedemo.com/inventory.html')
    driver.maximize_window()
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    elements_by_id = driver.find_elements(By.XPATH, "//*[@id]")
    for element in elements_by_id:
        my_logger.info(f'We found element by ID. This tag "{element.tag_name}" has "id": "{element.get_attribute("id")}"')

    element_by_name = driver.find_elements(By.XPATH, "//*[@name]")
    for element in element_by_name:
        my_logger.info(f'We found element by NAME. This tag "{element.tag_name}" has "name": "{element.get_attribute("name")}"')

    element_by_class = driver.find_elements(By.XPATH, "//*[@class]")
    for element in element_by_class:
       my_logger.info(f'We found elements by CLASS NAME. This tag "{element.tag_name}", has "class": {element.get_attribute("class")}')
