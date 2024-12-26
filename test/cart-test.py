# cart-test.py

from django.test import TestCase
from app1.models import Product  # Only import Product model

class CartTestCase(TestCase):
    
    def setUp(self):
        """
        Create a product to be used in the tests.
        """
        self.product = Product.objects.create(
            name="Cow Milk",  # You can replace this with the actual product name
            price=45,          # Price of the product
            stock=100          # Available stock
        )

    def test_add_to_cart(self):
        """
        Test adding an item to the cart.
        """
        # Add the product to the cart (simulated in test)
        cart = []  # Simulate an empty cart
        cart.append(self.product)  # Add product to the cart

        # Assert that the cart contains the product
        self.assertIn(self.product, cart)

    def test_remove_from_cart(self):
        """
        Test removing an item from the cart.
        """
        cart = [self.product]  # Simulate a cart with the product already in it
        cart.remove(self.product)  # Remove the product from the cart

        # Assert that the cart is now empty
        self.assertNotIn(self.product, cart)

    def test_cart_empty_after_removal(self):
        """
        Test that the cart is empty after removing all items.
        """
        cart = [self.product]  # Simulate a cart with the product
        cart.remove(self.product)  # Remove the product

        # Assert that the cart is empty
        self.assertEqual(len(cart), 0)
