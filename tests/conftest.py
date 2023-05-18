import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        service_obj = Service(r'C:\Users\samrk\Downloads\chromedriver_win32_112\chromedriver.exe')

    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://www.aircanada.com/us/en/aco/home.html")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()