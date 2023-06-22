import time

from web_tests.helpers import user
from web_tests.pages.tourist_inventory_page import TouristInventory
from web_tests.scenarios.test_success_login import test_success_login


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
    """
    test_success_login(driver)

    tourist_inventory_page = TouristInventory(driver)
    time.sleep(5)
    tourist_inventory_page.inventory_steps(user)
