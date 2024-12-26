import unittest
from app import app

class AdminLoginTestCase(unittest.TestCase):

    def setUp(self):
        """Setup the test environment."""
        self.app = app.test_client()  # Flask test client
        self.app.testing = True

    def test_admin_login_valid(self):
        """Test the login functionality with valid admin credentials."""
        response = self.app.post('/admin', data={
            'username': 'admin',
            'password': 'admin123'
        })
        self.assertEqual(response.status_code, 302)  # 302 is the status code for a redirect
        self.assertIn(b'Welcome to the Admin Dashboard!', response.data)  # Check if redirected to the dashboard

    def test_admin_login_invalid(self):
        """Test the login functionality with invalid admin credentials."""
        response = self.app.post('/admin', data={
            'username': 'admin',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid credentials, please try again.', response.data)  # Check if error message is shown

if _name_ == '_main_':
    unittest.main()