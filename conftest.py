import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(4)
    driver.maximize_window()
    yield driver
    driver.quit()