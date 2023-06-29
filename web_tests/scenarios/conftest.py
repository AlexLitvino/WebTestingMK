import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

from web_tests.pages.page_with_logged_in_user import PageWithLoggedInUser


@pytest.fixture()
def driver():
    path = r''
    driver = Chrome(service=Service(path))
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://www.joinup.lt/')
    yield driver
    driver.quit()
