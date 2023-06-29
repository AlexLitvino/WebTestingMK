from web_tests.pages.success_login import login_user


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

    login_user(driver)
