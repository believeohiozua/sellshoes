import pytest

from rest_framework.test import APIClient

from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

@pytest.fixture
def api_client():
    """Fixture to provide API client."""
    return APIClient()

@pytest.fixture
def signup_url():
    """Fixture for signup endpoint URL."""
    return reverse("signup")  # Replace 'signup' with your URL pattern name

@pytest.fixture
def valid_user_data():
    """Fixture for valid user signup data."""
    return {
        "email": "validuser@example.com",
        "first_name": "Valid",
        "last_name": "User",
        "password": "strongpassword123",
        "confirm_password": "strongpassword123",
    }

@pytest.mark.django_db
def test_successful_signup(api_client, signup_url, valid_user_data):
    """Test successful signup with valid and unique details."""
    response = api_client.post(signup_url, valid_user_data)
    assert response.status_code == 201
    assert response.data["message"] == "Signup successful"
    assert response.data["data"]["email"] == valid_user_data["email"]
    assert User.objects.filter(email=valid_user_data["email"]).exists()

@pytest.mark.django_db
def test_duplicate_email_signup(api_client, signup_url, valid_user_data):
    """Test duplicate email signup."""
    # Create a user with the same email
    User.objects.create_user(
        email=valid_user_data["email"],
        first_name="Existing",
        last_name="User",
        password="existingpassword123",
    )
    response = api_client.post(signup_url, valid_user_data)
    assert response.status_code == 400
    assert "custom user with this email already exists." in str(response.data["error"]["email"][0])


@pytest.mark.django_db
def test_invalid_email_signup(api_client, signup_url, valid_user_data):
    """Test invalid email format."""
    invalid_data = valid_user_data.copy()
    invalid_data["email"] = "invalidemail"
    response = api_client.post(signup_url, invalid_data)
    assert response.status_code == 400
    assert "Enter a valid email address." in response.data["error"]["email"]
