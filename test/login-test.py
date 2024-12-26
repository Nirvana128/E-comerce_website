from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginFunctionTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.login_url = reverse('login')  # Ensure this matches the correct login URL name in your app

    def test_login_success(self):
        """Test successful login with correct credentials."""
        # Log in with the correct credentials
        response = self.client.post(self.login_url, {
            'username': 'testuser',  # Use the test user created in setUp
            'password': 'testpassword',  # Use the password provided during user creation
        })
        
        # Check if the login redirects successfully
        self.assertEqual(response.status_code, 302)  # This should redirect on successful login
        
        # You can also check the page content after redirection if applicable
        # For example, after login, if the user is redirected to a welcome page:
        #self.assertRedirects(response, reverse('welcome'))  # Adjust 'welcome' to your redirect target

    def test_login_failure_incorrect_credentials(self):
        """Test login with incorrect credentials."""
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'wrongpassword',  # Incorrect password
        })
        self.assertEqual(response.status_code, 200)  # Stay on the login page
        self.assertContains(response, "Please enter a correct username and password. Note that both fields may be case-sensitive.")  # Adjust based on the actual error message in the template

    def test_login_failure_empty_fields(self):
        """Test login with empty username and password."""
        response = self.client.post(self.login_url, {
            'username': '',
            'password': '',
        })
        self.assertEqual(response.status_code, 200)  # Stay on the login page
        self.assertContains(response, "This field is required")  # Update to match actual validation message

    def test_login_failure_nonexistent_user(self):
        """Test login attempt with a nonexistent user."""
        response = self.client.post(self.login_url, {
            'username': 'nonexistent',  # A username that doesn't exist
            'password': 'password',
        })
        self.assertEqual(response.status_code, 200)  # Stay on the login page
        self.assertContains(response, "Please enter a correct username and password. Note that both fields may be case-sensitive.")  # Adjust based on actual error message
