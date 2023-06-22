import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service



from selenium.webdriver.common.by import By

path = r''


def test_success_login():
    driver = Chrome(service=Service(path))
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://www.joinup.lt/')

    cookie_popup = driver.find_element(By.ID, "__layout")
    time.sleep(4)
    if cookie_popup.is_displayed():
        cookie_accept = driver.find_element(By.XPATH, "(//button[@class='info-modal__btn btn-3'])[2]")
        cookie_accept.click()

    time.sleep(8)
    login_button = driver.find_element(By.XPATH, "(//div[@class='header-cabinet header__cabinet'])[1]")
    login_button.click()
    time.sleep(3)

    sign_in_tab = driver.find_element(By.XPATH, "(//a[@class='tabs-component-tab-a'])[2]")
    sign_in_tab.click()


    valid_user = 'kobamaryna@gmail.com'
    valid_password = 'summer'

    # username_input_field = driver.find_element(By.NAME, 'email')
    username_input_field = driver.find_element(By.XPATH, "(// input[@ name='email'])[4]")
    password_input_field = driver.find_element(By.NAME, 'password')
    username_input_field.send_keys(valid_user)
    password_input_field.send_keys(valid_password)
    time.sleep(1)
    login_button = driver.find_element(By.XPATH, '//button[@class="login-account__submit btn-1"]')
    login_button.click()
    time.sleep(1)
    tourist_name = driver.find_element(By.XPATH, '//div[@class="header-cabinet__name"]')
    time.sleep(2)
    assert tourist_name.is_displayed()

    driver.quit()


def test_check_tourist_inventory():
    driver = Chrome(service=Service(path))
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://www.joinup.lt/')

    cookie_popup = driver.find_element(By.ID, "__layout")
    time.sleep(4)
    if cookie_popup.is_displayed():
        cookie_accept = driver.find_element(By.XPATH, "(//button[@class='info-modal__btn btn-3'])[2]")
        cookie_accept.click()

    time.sleep(8)
    login_button = driver.find_element(By.XPATH, "(//div[@class='header-cabinet header__cabinet'])[1]")
    login_button.click()
    time.sleep(3)

    sign_in_tab = driver.find_element(By.XPATH, "(//a[@class='tabs-component-tab-a'])[2]")
    sign_in_tab.click()

    valid_user = 'kobamaryna@gmail.com'
    valid_password = 'summer'

    # username_input_field = driver.find_element(By.NAME, 'email')
    username_input_field = driver.find_element(By.XPATH, "(// input[@ name='email'])[4]")
    password_input_field = driver.find_element(By.NAME, 'password')
    username_input_field.send_keys(valid_user)
    password_input_field.send_keys(valid_password)
    time.sleep(1)

    login_button = driver.find_element(By.XPATH, '//button[@class="login-account__submit btn-1"]')
    login_button.click()

    time.sleep(5)
    tourist_inventory = driver.find_element(By.XPATH, '(//div[@class="header-cabinet header__cabinet"])[1]')
    tourist_inventory.click()
    time.sleep(2)
    account_settings = driver.find_element(By.XPATH, '(//div[@class ="header-cabinet__dropdown-item"])[1]')
    account_settings.click()

    time.sleep(2)
    tourist_inventory = driver.find_element(By.XPATH, '(//div[@class="header-cabinet header__cabinet"])[1]')
    tourist_inventory.click()
    time.sleep(2)
    my_tours = driver.find_element(By.XPATH, '(//div[@class ="header-cabinet__dropdown-item"])[1]')
    my_tours.click()

    time.sleep(2)
    tourist_inventory = driver.find_element(By.XPATH, '(//div[@class="header-cabinet header__cabinet"])[1]')
    tourist_inventory.click()
    time.sleep(2)
    favorite_hotels = driver.find_element(By.XPATH, '(//div[@class ="header-cabinet__dropdown-item"])[2]')
    favorite_hotels.click()

    time.sleep(2)
    tourist_inventory = driver.find_element(By.XPATH, '(//div[@class="header-cabinet header__cabinet"])[1]')
    tourist_inventory.click()
    time.sleep(2)
    log_out = driver.find_element(By.XPATH, '(//div[@class ="header-cabinet__dropdown-item"])[3]')
    log_out.click()
    time.sleep(2)

    driver.quit()

def test_change_language():
    driver = Chrome(service=Service(path))
    driver.maximize_window()
    driver.implicitly_wait(9)
    driver.get('https://www.joinup.lt/')

    cookie_popup = driver.find_element(By.ID, "__layout")
    time.sleep(4)
    if cookie_popup.is_displayed():
        cookie_accept = driver.find_element(By.XPATH, "(//button[@class='info-modal__btn btn-3'])[2]")
        cookie_accept.click()


    time.sleep(8)
    language_button = driver.find_element(By.XPATH, '(//div[@class ="header-lang"])[2]')
    language_button.click()
    time.sleep(4)
    new_button = driver.find_element(By.XPATH, '//ul[@class ="header-lang__list header-lang__list--visible"]')
    new_button.click()
    driver.quit()


def test_check_cream_results():
    driver = Chrome(service=Service(path))
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://www.joinup.lt/')

    cookie_popup = driver.find_element(By.ID, "__layout")
    time.sleep(4)
    if cookie_popup.is_displayed():
        cookie_accept = driver.find_element(By.XPATH, "(//button[@class='info-modal__btn btn-3'])[2]")
        cookie_accept.click()

    time.sleep(8)

    cream_block = driver.find_element(By.XPATH, "(//article[@class='tour-card'])[1]")
    cream_block.click()
    assert cream_block.is_displayed()

    departure_date = driver.find_element(By.XPATH, "//input[@class ='input-field__input datepicker__input form-control input']")
    time.sleep(4)
    departure_date.click()
    span_element = driver.find_element(By.XPATH, "//span[@class='flatpickr-day' and @tabindex='-1']")
    assert span_element is not None, "Test failed: span element with tabindex='-1' not found"

    driver.quit()