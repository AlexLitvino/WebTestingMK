from web_tests.helpers.user import User
from web_tests.pages.cookie_policy_on_page import cookie_modal_window
from web_tests.pages.login_page import LoginPage


def test_success_login(driver):
    """
    1. Go to URL
    2. If we have cookie_police message - accept them
    3. Click to Login Button
    4. Move to SignIn tab
    5. Enter email and password
    6. Click SignIn button
    """
    cookie_modal_window(driver)

    user = User('kobamaryna@gmail.com', 'summer')
    login_page = LoginPage(driver)
    login_page.fill_login_form(user)
    login_page.successful_login(user)
    # what should be checked here?
    assert login_page.tourist_name.text == 'Maryna'  # maybe this?
