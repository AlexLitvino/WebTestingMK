from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def cookie_modal_window(driver):
    wait = WebDriverWait(driver, 5)
    cookie_accept = wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[@class='info-modal__btn btn-3'])[2]")))
    cookie_accept.click()
