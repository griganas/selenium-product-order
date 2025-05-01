from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_field = (By.CLASS_NAME, "search-keyword")
        self.search_button = (By.CLASS_NAME, "search-button")
        self.add_to_cart_button = (By.XPATH, "//div[2]//div[3]//button[1]")
        self.cart_icon = (By.CLASS_NAME, "cart-icon")
        self.proceed_button = (By.CLASS_NAME, "action-block")
        self.promo_code_input = (By.CLASS_NAME, "promoCode")
        self.promo_button = (By.CSS_SELECTOR, ".promoBtn")
        self.promo_message = (By.CSS_SELECTOR, ".promoInfo")
        self.discount_amount = (By.CLASS_NAME, "discountAmt")
        self.place_order_button = (By.XPATH, "//button[normalize-space()='Place Order']")
        self.dropdown = (By.XPATH, "//div[@class='wrapperTwo']//div//select")
        self.agree_checkbox = (By.CLASS_NAME, "chkAgree")
        self.proceed_to_order = (By.CSS_SELECTOR, "div[class='wrapperTwo'] button")

    def search_product(self, text):
        self.driver.find_element(*self.search_field).send_keys(text)
        self.driver.find_element(*self.search_button).click()

    def add_first_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.cart_icon).click()
        self.driver.find_element(*self.proceed_button).click()

    def apply_promo_code(self, code):
        self.driver.find_element(*self.promo_code_input).send_keys(code)
        self.driver.find_element(*self.promo_button).click()

    def get_promo_message(self):
        return self.driver.find_element(*self.promo_message).text

    def get_discount_amount(self):
        return self.driver.find_element(*self.discount_amount).text

    def place_order(self, country="Greece"):
        self.driver.find_element(*self.place_order_button).click()
        Select(self.driver.find_element(*self.dropdown)).select_by_value(country)
        self.driver.find_element(*self.agree_checkbox).click()
        self.driver.find_element(*self.proceed_to_order).click()
