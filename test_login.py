import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_exitoso():
    driver = webdriver.Chrome()

    wait = WebDriverWait (driver, 10)

    try:
        #login
        driver.get ("https://www.saucedemo.com/")

        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys ("standard_user")
        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys ("secret_sauce")
        wait.until (EC.element_to_be_clickable((By.ID, "login-button"))).click()

        #validaciones
        assert "/inventory.html" in driver.current_url

        logo = driver.find_element (By.CLASS_NAME, "app_logo")
        assert logo.text == "Swag Labs"

        titulo = driver.find_element (By.CSS_SELECTOR, "[data-test='title']")
        assert titulo.text == "Products"

    finally:
        driver.quit()