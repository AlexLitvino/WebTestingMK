import time

from selenium.webdriver.common.by import By
from web_tests.pages.cookie_policy_on_page import cookie_modal_window
from web_tests.pages.login_page import LoginPage


def test_change_language(driver):
    """
    1. Go to URL
    2. If we have cookie_police message - accept them
    3. Click language button
    4. Change the language
    5. Check that language is changed
    """
    cookie_modal_window(driver)
    login_page = LoginPage(driver)
    login_page.change_language()
    assert login_page.search_for_tour_button.is_displayed()
    assert login_page.search_for_tour_button.text == 'PAIEŠKA'

    # language_button = driver.find_element(By.XPATH, '(//div[@class ="header-lang"])[2]')
    # language_button.click()
    # time.sleep(3)

    # new_button = driver.find_element(By.XPATH, '//ul[@class ="header-lang__list header-lang__list--visible"]')
    # new_button.click()
    # time.sleep(3)

    # check_translated_word = driver.find_element(By.XPATH, "//*[text() = 'Paieška']")
    # assert check_translated_word.is_displayed()

