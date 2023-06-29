import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_tests.helpers import user
#from web_tests.pages.success_login import login_user
from web_tests.helpers.user import User
from web_tests.pages.cookie_policy_on_page import cookie_modal_window
from web_tests.pages.login_page import LoginPage
from web_tests.pages.tourist_inventory_page import TouristInventory


def test_check_tourist_inventory(driver):
    """
    1. Go to URL
    2. If we have cookie_police message - accept them
    3. Click to Login Button
    4. Move to SignIn tab
    5. Enter email and password
    6. Click SignIn button
    7. Click account button
    8. Choose first point of dropdown
    9. Choose second point of dropdown
    10. Choose third point of dropdown
    11. Choose fourth point of dropdown
    12. Check that all dropdowns are clickable
    # Here I was confused. In inventory_steps(self, user): we click and click again but don't verify anything.
     We need to check that some unique element is displayed after each click.
    """
    #login_user(driver)
    cookie_modal_window(driver)
    user = User('kobamaryna@gmail.com', 'summer')
    login_page = LoginPage(driver)
    page_with_logged_in_user = login_page.perform_successful_login(user)
    menu_page = page_with_logged_in_user.click_tourist_inventory_button()
    tourist_inventory_page = menu_page.click_account_settings_button()
    tourist_inventory_page.click_log_out()
    wait = WebDriverWait(driver, 5)
    check_log_out = wait.until((EC.visibility_of_element_located((By.XPATH, "//button[normalize-space(.) = 'Login']"))))
    assert check_log_out.is_displayed()


    # tourist_inventory_page = TouristInventory(driver)
    # time.sleep(5)
    # tourist_inventory_page.inventory_steps(user)
    #
    # check_log_out = driver.find_element(By.XPATH, "//button[normalize-space(.) = 'Login']")
    # assert check_log_out.is_displayed()
