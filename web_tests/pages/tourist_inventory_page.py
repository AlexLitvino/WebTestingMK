from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TouristInventory:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @property
    def tourist_inventory_button(self):
        return self.driver.find_element(By.XPATH, '(//div[@class="header-cabinet header__cabinet"])[1]')

    @property
    def account_settings(self):
        return self.driver.find_element(By.XPATH, '(//div[@class ="header-cabinet__dropdown-item"])[1]')

    @property
    def my_tours(self):
        return self.driver.find_element(By.XPATH, '(//div[@class ="header-cabinet__dropdown-item"])[1]')

    @property
    def favorite_hotels(self):
        return self.driver.find_element(By.XPATH, '(//div[@class ="header-cabinet__dropdown-item"])[2]')

    @property
    def log_out(self):
        return self.driver.find_element(By.XPATH, '(//div[@class ="header-cabinet__dropdown-item"])[3]')

    def click_tourist_inventory_button(self):
        tourist_inventory_button = self.tourist_inventory_button
        WebDriverWait(self.driver, 12).until(EC.element_to_be_clickable(tourist_inventory_button))
        tourist_inventory_button.click()

    def click_account_settings_button(self):
        account_settings = self.account_settings
        WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable(account_settings))
        account_settings.click()
        WebDriverWait(self.driver, 9).until(EC.invisibility_of_element(account_settings))

    def click_my_tours_button(self):
        my_tours = self.my_tours
        WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable(my_tours))
        my_tours.click()
        WebDriverWait(self.driver, 9).until(EC.invisibility_of_element(my_tours))

    def click_favorite_hotels_button(self):
        favorite_hotels = self.favorite_hotels
        WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable(favorite_hotels))
        favorite_hotels.click()
        WebDriverWait(self.driver, 9).until(EC.invisibility_of_element(favorite_hotels))

    def click_log_out(self):
        log_out = self.log_out
        WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable(log_out))
        log_out.click()
        WebDriverWait(self.driver, 9).until(EC.invisibility_of_element(log_out))

    def inventory_steps(self, user):
        self.click_tourist_inventory_button()
        self.click_account_settings_button()
        self.click_tourist_inventory_button()
        self.click_my_tours_button()
        self.click_tourist_inventory_button()
        self.click_favorite_hotels_button()
        self.click_tourist_inventory_button()
        self.click_log_out()

