import pickle


def test_registration(registration):
    """Test registration"""
    driver = registration
    driver.get('https://www.saucedemo.com/inventory.html')
    driver.maximize_window()
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    title = driver.title
    assert title == "Swag Labs"
