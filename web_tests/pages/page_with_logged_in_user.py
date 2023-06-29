from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from web_tests.pages.base_page import BasePage
from web_tests.pages.menu_page import MenuPage


class PageWithLoggedInUser(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def tourist_name(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="header-cabinet__name"]')))

    @property
    def tourist_inventory_button(self):
        return self.driver.find_element(By.XPATH, '(//div[@class="header-cabinet header__cabinet"])[1]')


    def click_tourist_inventory_button(self):
        self.tourist_inventory_button.click()
        return MenuPage(self.driver)

    #




    # def do_something_on_next_page(self):
    #     pass

