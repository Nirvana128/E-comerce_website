from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginFunctionTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.login_url = reverse('login')  # Update 'login' to your actual URL name

    def test_login_success(self):
        """Test successful login with correct credentials."""
        response = self.client.post(self.login_url, {
            'username': 'nirvana1',
            'password': '12345rrr',
        })
        self.assertEqual(response.status_code, 200)  # Adjust based on your success redirection
        self.assertContains(response, "Welcome")  # Replace with your success message/content

    def test_login_failure_incorrect_credentials(self):
        """Test login with incorrect credentials."""
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid credentials")  # Replace with your error message

    def test_login_failure_empty_fields(self):
        """Test login with empty username and password."""
        response = self.client.post(self.login_url, {
            'username': '',
            'password': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")  # Replace with your validation message

    def test_login_failure_nonexistent_user(self):
        """Test login attempt with a nonexistent user."""
        response = self.client.post(self.login_url, {
            'username': 'nonexistent',
            'password': 'password',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid credentials")  # Replace with your error message
