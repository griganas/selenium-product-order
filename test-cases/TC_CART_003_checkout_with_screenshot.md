Test Case ID: TC_CART_003
Title: Product Checkout with Valid Promo Code and Screenshot Capture

Test Scenario:
The user adds a product to the cart, applies a valid promo code, completes the order, and captures a screenshot of the confirmation page.

Preconditions:
User is on the homepage: https://rahulshettyacademy.com/seleniumPractise/#/
Browser is open and functional

Test Steps:
1. Search for a product using the keyword ap
2. Wait for product results to appear
3. Add the first product to the cart
4. Proceed to checkout
5. Enter promo code: rahulshettyacademy
6. Click to apply the promo code
7. Wait for confirmation
8. Verify discount was applied
9. Place the order
10. Capture a screenshot of the final screen
    
Expected Result:
Promo code is applied successfully with the message “Code applied”
Discount is greater than 0
Order is completed
Screenshot is saved (e.g., screen.png)

Postconditions:
The product is purchased successfully and the screenshot is stored.

Status: Pass

Automated Test:
Implemented in test_cart_functions.py, function: test_product_checkout

