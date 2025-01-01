from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from unittest.mock import patch, MagicMock
from ..app1.models import Cart, Wishlist, OrderPlaced
from ..app1.views import orders
import unittest

class TestOrdersView(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.factory = RequestFactory()

    @patch('app1.models.Cart.objects.filter')
    @patch('app1.models.Wishlist.objects.filter')
    @patch('app1.models.OrderPlaced.objects.filter')
    def test_orders_view_authenticated_user_no_orders(
        self, mock_order_placed_filter, mock_wishlist_filter, mock_cart_filter
    ):
        # Mock the Cart, Wishlist, and OrderPlaced queries
        mock_cart_filter.return_value = []
        mock_wishlist_filter.return_value = []
        mock_order_placed_filter.return_value.exists.return_value = False

        # Simulate a GET request as an authenticated user
        request = self.factory.get('/orders/')
        request.user = self.user

        # Call the view
        response = orders(request)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"You have no orders yet.", response.content)
        self.assertEqual(mock_cart_filter.call_count, 1)
        self.assertEqual(mock_wishlist_filter.call_count, 1)
        self.assertEqual(mock_order_placed_filter.call_count, 1)

if _name_ == '_main_':
    unittest.main()