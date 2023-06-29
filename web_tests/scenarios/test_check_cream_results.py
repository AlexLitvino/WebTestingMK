import time

from selenium.webdriver.common.by import By
from web_tests.pages.cookie_policy_on_page import cookie_modal_window


def test_check_cream_results(driver):
    """
    1. Go to URL
    2. If we have cookie_police message - accept them
    3. Click first hotel from Cream block
    4. Check available dates in datepicker
    """
    cookie_modal_window(driver)
    cream_block = driver.find_element(By.XPATH, "(//article[@class='tour-card'])[1]")
    cream_block.click()
    assert cream_block.is_displayed()

    time.sleep(6)
    departure_date = driver.find_element(By.XPATH, "//div[@class='flatpickr-wrapper']")
    departure_date.click()
    span_element = driver.find_element(By.XPATH, "//span[@class='flatpickr-day' and @tabindex='-1']")
    assert span_element is not None, "Test failed: dates not found"
