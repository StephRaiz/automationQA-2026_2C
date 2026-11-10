import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_inventory():
    driver = webdriver.Chrome()

    wait = WebDriverWait (driver, 10)

    try:
        #login
        driver.get ("https://www.saucedemo.com/")

        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys ("standard_user")
        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys ("secret_sauce")
        wait.until (EC.element_to_be_clickable((By.ID, "login-button"))).click()

        #validaciones
        assert driver.title == "Swag Labs"

        productos = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
        assert len(productos) > 0

        primer_producto = productos[0]
        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

        assert nombre_producto == "Sauce Labs Backpack"
        assert precio_producto == "$29.99"

        menu = driver.find_element (By.ID , "react-burger-menu-btn")
        assert menu.is_displayed()

        filtro = driver.find_element (By.CLASS_NAME, "product_sort_container")
        assert filtro.is_displayed()
    

    finally:
        driver.quit()