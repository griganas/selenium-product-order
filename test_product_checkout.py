import time
from ProductPage import ProductPage

def test_product_checkout(driver):
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    page = ProductPage(driver)

    page.search_product("ap")
    time.sleep(3)
    page.add_first_product_to_cart()
    page.proceed_to_checkout()
    page.apply_promo_code("rahulshettyacademy")
    time.sleep(5)

    assert "Code applied" in page.get_promo_message()
    assert float(page.get_discount_amount()) > 0

    page.place_order()
    driver.get_screenshot_as_file("screen.png")
