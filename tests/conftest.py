import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver(request):
    if request.config.getoption("--browser") == "chrome":
        my_driver = webdriver.Chrome()
    elif request.config.getoption("--browser") == "firefox":
        my_driver = webdriver.Firefox()
    else:
        raise ValueError(f"Invalid value. Expected chrome or firefox but got {request.config.getoption('--browser')}")
    my_driver.implicitly_wait(10)
    yield my_driver
    my_driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Please specify which browser to test on")
