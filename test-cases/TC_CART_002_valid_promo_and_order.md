Test Case ID: TC_CART_002
Title: Apply Valid Promo Code and Place Order for a Different Product and Country

Test Scenario:
User applies a valid promo code, sees the discount applied, and successfully places the order for a different product and country.

Preconditions:
User is on the homepage: https://rahulshettyacademy.com/seleniumPractise/#/
Browser is open and working

Test Steps:
1. Search for a product using the keyword be
2. Wait for products to appear
3. Add the first product to the cart
4. Proceed to checkout
5. Enter promo code: rahulshettyacademy
6. Click to apply the promo code
7. Wait for confirmation message
8. Verify that a discount was applied
9. Select country: India
10. Place the order

Expected Result:
A message confirming the promo code appears (“Code applied”). A discount is applied. Order is placed successfully for India.

Postconditions:
User completes the purchase.

Status: Pass

Automated Test:
Implemented in test_cart_functions.py, function: test_checkout_different_product_and_country

