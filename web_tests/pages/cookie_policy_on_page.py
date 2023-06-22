from selenium.webdriver.common.by import By
import time


def cookie_modal_window(driver):
    cookie_popup = driver.find_element(By.ID, "__layout")
    cookie_accept = driver.find_element(By.XPATH, "(//button[@class='info-modal__btn btn-3'])[2]")

    if cookie_popup.is_displayed():
        time.sleep(4)
        cookie_accept.click()
