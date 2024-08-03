import pytest
from selenium import webdriver
import logging as logger


@pytest.fixture(scope="session")
def driver(request):
    if request.config.getoption("--browser") == "chrome":
        logger.info("Launching Tests on Chrome")
        my_driver = webdriver.Chrome()
    elif request.config.getoption("--browser") == "firefox":
        logger.info("Launching Tests on FireFox")
        my_driver = webdriver.Firefox()
    else:
        raise TypeError(f"Invalid value. Expected chrome or firefox but got {request.config.getoption('--browser')}")
    # my_driver.implicitly_wait(10)
    yield my_driver
    my_driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Please specify which browser to test on")
