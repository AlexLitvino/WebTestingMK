from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_tests.pages.base_page import BasePage
from web_tests.pages.page_with_logged_in_user import PageWithLoggedInUser


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver
        # self.wait = WebDriverWait(driver, 5)

    @property
    def email_input_field(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@ name='email'])[4]")))

    @property
    def password_input_field(self):
        return self.wait.until(EC.visibility_of_element_located((By.NAME, 'password')))

    @property
    def login_button(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='header-cabinet header__cabinet'])[1]")))

    @property
    def signin_tab(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[@class='tabs-component-tab-a'])[2]")))

    @property
    def signin_button(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="login-account__submit btn-1"]')))

    @property
    def language_button(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class ="header-lang"])[2]')))

    @property
    def new_language_button(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@class ="header-lang__list header-lang__list--visible"]')))

    @property
    def search_for_tour_button(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//ul[contains(@class, 'header-nav__inner')]/li[1]/a/span[1]")))



    # this is element from page with logged in user
    # @property
    # def tourist_name(self):
    #     return self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="header-cabinet__name"]')))

    def click_login_button(self):
        # login_button = self.login_button
        # WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable(login_button))
        self.login_button.click()

    def click_signin_tab(self):
        # signin_tab = self.signin_tab
        # WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable(signin_tab))
        self.signin_tab.click()

    def enter_email(self, email):
        self.email_input_field.send_keys(email)
        return self

    def enter_password(self, password):
        self.password_input_field.send_keys(password)
        return self

    def click_signin_button(self):
        # signin_button = self.signin_button
        # WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable(signin_button))
        # signin_button.click()
        # WebDriverWait(self.driver, 9).until(EC.invisibility_of_element(signin_button))
        self.signin_button.click()

    def perform_successful_login(self, user):
        self.click_login_button()
        self.click_signin_tab()
        self.enter_email(user.email)
        self.enter_password(user.password)
        self.click_signin_button()
        return PageWithLoggedInUser(self.driver)

    def click_language_button(self):
        self.language_button.click()

    def click_new_language_button(self):
        self.new_language_button.click()


    def change_language(self):
        self.click_language_button()
        self.click_new_language_button()


    # def successful_login(self, user):
    #     return self.tourist_name
