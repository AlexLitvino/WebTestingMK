from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from web_tests.pages.base_page import BasePage
from web_tests.pages.tourist_inventory_page import TouristInventory


class MenuPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def account_settings(self):
        return self.wait.until((EC.visibility_of_element_located((By.XPATH, '(//div[@class ="header-cabinet__dropdown-item"])[1]'))))

    def click_account_settings_button(self):
        self.account_settings.click()
        return TouristInventory(self.driver)
        # account_settings = self.account_settings
        # WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable(account_settings))
        # account_settings.click()
        # WebDriverWait(self.driver, 9).until(EC.invisibility_of_element(account_settings))