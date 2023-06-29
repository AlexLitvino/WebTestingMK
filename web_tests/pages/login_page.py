from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_tests.pages.page_with_logged_in_user import PageWithLoggedInUser


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @property
    def email_input_field(self):
        return self.driver.find_element(By.XPATH, "(//input[@ name='email'])[4]")

    @property
    def password_input_field(self):
        return self.driver.find_element(By.NAME, 'password')

    @property
    def login_button(self):
        return self.driver.find_element(By.XPATH, "(//div[@class='header-cabinet header__cabinet'])[1]")

    @property
    def signin_tab(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[@class='tabs-component-tab-a'])[2]")))

    @property
    def signin_button(self):
        return self.driver.find_element(By.XPATH, '//button[@class="login-account__submit btn-1"]')

    @property
    def tourist_name(self):
        return self.driver.find_element(By.XPATH, '//div[@class="header-cabinet__name"]')

    def click_login_button(self):
        login_button = self.login_button
        WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable(login_button))
        login_button.click()

    def click_signin_tab(self):
        signin_tab = self.signin_tab
        WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable(signin_tab))
        signin_tab.click()

    def enter_email(self, email):
        self.email_input_field.send_keys(email)
        return self

    def enter_password(self, password):
        self.password_input_field.send_keys(password)
        return self

    def click_signin_button(self):
        signin_button = self.signin_button
        WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable(signin_button))
        signin_button.click()
        WebDriverWait(self.driver, 9).until(EC.invisibility_of_element(signin_button))

    def fill_login_form(self, user):
        self.click_login_button()
        self.click_signin_tab()
        self.enter_email(user.email)
        self.enter_password(user.password)
        self.click_signin_button()
        return PageWithLoggedInUser()

    def successful_login(self, user):
        return self.tourist_name
