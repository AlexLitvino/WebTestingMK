from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_tests.pages.base_page import BasePage


class TouristInventory(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver
        # self.wait = WebDriverWait(driver, 5)

    @property
    def my_tours(self):
        return self.wait.until(EC.visibility_of_element_located(((By.XPATH, '(//div[@class ="header-cabinet__dropdown-item"])[1]'))))

    @property
    def favorite_hotels(self):
        return self.wait.until(EC.visibility_of_element_located(((By.XPATH, '(//div[@class ="header-cabinet__dropdown-item"])[2]'))))

    @property
    def log_out(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[contains(@class, 'btn-3')])[1]")))
        #return self.wait.until(EC.visibility_of_element_located(((By.XPATH, '(//div[@class ="header-cabinet__dropdown-item"])[3]'))))

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
        self.log_out.click()

    def inventory_steps(self, user):
        self.click_tourist_inventory_button()
        self.click_account_settings_button()
        self.click_tourist_inventory_button()
        self.click_my_tours_button()
        self.click_tourist_inventory_button()
        self.click_favorite_hotels_button()
        self.click_tourist_inventory_button()
        self.click_log_out()

