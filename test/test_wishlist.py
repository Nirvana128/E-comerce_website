from django.test import TestCase, Client
from django.contrib.auth.models import User
from app1.models import Product, Wishlist
import unittest 

class WishlistTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='12345')
        # Create a product
        self.product = Product.objects.create(name='Test Product', price=10)
        # Set up the client
        self.client = Client()
        # Log in the user
        self.client.login(username='testuser', password='12345')
    
    def test_add_to_wishlist(self):
        # Use the product id to add to the wishlist
        response = self.client.get(f'/add_to_wishlist?prod_id={self.product.id}')
        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        # Check that the message returned is correct
        self.assertJSONEqual(response.content, {'message': 'Wishlist Added Successfully'})
        # Check that the Wishlist item has been created
        wishlist_count = Wishlist.objects.filter(user=self.user, product=self.product).count()
        self.assertEqual(wishlist_count, 1)

# This test checks whether the product is correctly added to the user's wishlist
# and verifies that the response is what we expect.
if __name__ == '__main__':
    unittest.main()
