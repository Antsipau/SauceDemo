import time
import pickle
from selenium.webdriver.common.by import By


def test_show_items(registration, my_logger):
    """Find items and prices far all goods"""
    driver = registration
    driver.get('https://www.saucedemo.com/inventory.html')
    driver.maximize_window()
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    items = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')  # Try to find all items in inventory by name.
    list_of_items = []  # Empty list for items.
    for item in items:
       list_of_items.append(item.text)  # Add all items into list.

    prices = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')  # Try to find all prices in inventory.
    list_of_prices = []  # Empty list for prices.
    for price in prices:
       list_of_prices.append(price.text)  # Add all items into list.

    full_info = dict(zip(list_of_items, list_of_prices))  # Dictionary with items and prices for them
    assert full_info == {'Sauce Labs Backpack': '$29.99', 'Sauce Labs Bike Light': '$9.99',
                         'Sauce Labs Bolt T-Shirt': '$15.99', 'Sauce Labs Fleece Jacket': '$49.99',
                         'Sauce Labs Onesie': '$7.99', 'Test.allTheThings() T-Shirt (Red)': '$15.99'}

    for k, v in full_info.items():
        my_logger.info(f'This product: "{k}" costs {v}')

    time.sleep(5)
