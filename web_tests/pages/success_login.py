from web_tests.helpers.user import User
from web_tests.pages.cookie_policy_on_page import cookie_modal_window
from web_tests.pages.login_page import LoginPage


def login_user(driver):
    cookie_modal_window(driver)
    user = User('kobamaryna@gmail.com', 'summer')
    login_page = LoginPage(driver)
    login_page.fill_login_form(user)
    login_page.successful_login(user)
    assert login_page.tourist_name.text == 'Maryna'
