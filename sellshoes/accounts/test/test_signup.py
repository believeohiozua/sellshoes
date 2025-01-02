import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()

@pytest.fixture
def api_client():
    """Fixture to provide an API client."""
    return APIClient()

@pytest.fixture
def create_user():
    """Fixture to create a user in the database."""
    def _create_user(email, first_name, last_name, password):
        return User.objects.create_user(email=email, first_name=first_name, last_name=last_name, password=password)
    return _create_user

@pytest.mark.django_db
class TestSignupEndpoint:
    endpoint = "/accounts/signup/"  # Replace with your actual signup endpoint URL

    def test_successful_signup(self, api_client):
        """Verify that a user can sign up with valid and unique details."""
        payload = {
            "email": "testuser@example.com",
            "first_name": "Test",
            "last_name": "User",
            "password": "password123",
            "confirm_password": "password123",
        }
        response = api_client.post(self.endpoint, payload)
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.filter(email="testuser@example.com").exists()

    def test_duplicate_email_signup(self, api_client, create_user):
        """Confirm that the endpoint returns an error for duplicate email."""
        create_user(
            email="duplicate@example.com",
            first_name="Existing",
            last_name="User",
            password="password123"
        )
        payload = {
            "email": "duplicate@example.com",
            "first_name": "New",
            "last_name": "User",
            "password": "password123",
            "confirm_password": "password123",
        }
        response = api_client.post(self.endpoint, payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "email" in response.data
        assert response.data["email"] == ["This email is already registered."]

    def test_invalid_email_format(self, api_client):
        """Ensure that an error is returned for invalid email formats."""
        payload = {
            "email": "invalid-email",
            "first_name": "Test",
            "last_name": "User",
            "password": "password123",
            "confirm_password": "password123",
        }
        response = api_client.post(self.endpoint, payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "email" in response.data
        assert response.data["email"] == ["Enter a valid email address."]


