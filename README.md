This repo contains some automation tests I made using Selenium and Python.

The website is a demo, and the test simulates a user searching for a product, adding it to the cart, using a promo code, and placing an order.

You can choose which browser to use (Chrome, Firefox, or Edge) by adding the `--browserName` option when running the test.

pytest test_product_checkout.py --browserName=firefox
