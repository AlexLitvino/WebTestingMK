from web_tests.helpers.user import User
from web_tests.pages.cookie_policy_on_page import cookie_modal_window
from web_tests.pages.login_page import LoginPage
#from web_tests.pages.success_login import login_user


def test_success_login(driver):
    """
    1. Go to URL
    2. If we have cookie_police message - accept them
    3. Click to Login Button
    4. Move to SignIn tab
    5. Enter email and password
    6. Click SignIn button
    7. Check that login is successful and user's name is viewed
    """
    cookie_modal_window(driver)
    user = User('kobamaryna@gmail.com', 'summer')
    login_page = LoginPage(driver)
    page_with_logged_in_user = login_page.perform_successful_login(user)
    # login_page.successful_login(user)
    assert page_with_logged_in_user.tourist_name.text == 'Maryna'

    #login_user(driver)
