import time
import pytest
from ProductPage import ProductPage

def test_invalid_promo_code(driver):
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    page = ProductPage(driver)

    page.search_product("ap")
    time.sleep(2)
    page.add_first_product_to_cart()
    page.proceed_to_checkout()
    page.apply_promo_code("invalidCode123")
    time.sleep(3)

    assert "Invalid" in page.get_promo_message()

def test_checkout_different_product_and_country(driver):
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    page = ProductPage(driver)

    page.search_product("be")
    time.sleep(2)
    page.add_first_product_to_cart()
    page.proceed_to_checkout()
    page.apply_promo_code("rahulshettyacademy")
    time.sleep(3)

    assert "Code applied" in page.get_promo_message()
    assert float(page.get_discount_amount()) > 0

    page.place_order("India")