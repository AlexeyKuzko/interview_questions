import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.base_page import BasePage
from data import TestData


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif request.param == "firefox":
        web_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    yield web_driver
    web_driver.quit()


@pytest.fixture(scope="class")
def base_page(init_driver):
    return BasePage(init_driver)


@pytest.fixture(scope="class")
def test_data():
    return TestData()