import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browserName", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture()
def driver(request):
    browserName = request.config.getoption("browserName")
    if browserName == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)

    elif browserName == "edge":
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(options=options)

    elif browserName == "firefox":
        options = webdriver.FirefoxOptions()
        options.page_load_strategy = 'normal'
        driver = webdriver.Firefox(options=options)

    driver.implicitly_wait(4)
    driver.maximize_window()

    yield driver
    driver.quit()