import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

path = r''

@pytest.fixture()
def driver():
    driver = Chrome(service=Service(path))
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://www.joinup.lt/')
    yield driver
    driver.quit()
