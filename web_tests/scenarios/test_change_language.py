import time

from selenium.webdriver.common.by import By
from web_tests.pages.cookie_policy_on_page import cookie_modal_window


def test_change_language(driver):
    """
    1. Go to URL
    2. If we have cookie_police message - accept them
    3. Click language button
    4. Change the language
    5. Check that language is changed
    """
    cookie_modal_window(driver)
    language_button = driver.find_element(By.XPATH, '(//div[@class ="header-lang"])[2]')
    language_button.click()
    time.sleep(3)

    new_button = driver.find_element(By.XPATH, '//ul[@class ="header-lang__list header-lang__list--visible"]')
    new_button.click()
    time.sleep(3)

    check_translated_word = driver.find_element(By.XPATH, "//*[text() = 'Paieška']")
    assert check_translated_word.is_displayed()
