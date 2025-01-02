import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def login_url():
    return '/accounts/login/'  # Adjust to your actual URL

@pytest.fixture
def create_user():
    """Create a sample user for testing."""
    def _create_user(email, password):
        return User.objects.create_user(email=email, password=password)
    return _create_user

@pytest.mark.django_db
def test_successful_login(api_client, login_url, create_user):
    """Test successful login with valid credentials."""
    user = create_user(email="testuser@example.com", password="securepassword123")
    response = api_client.post(login_url, {"email": "testuser@example.com", "password": "securepassword123"})
    assert response.status_code == 200
    assert response.data["message"] == "Login successful"
    assert "access_token" in response.data["data"]

    # Validate JWT token
    access_token = response.data["data"]["access_token"]
    token = AccessToken(access_token)
    assert str(token.payload["user_id"]) == str(user.id)

@pytest.mark.django_db
def test_invalid_email(api_client, login_url):
    """Test login with an email that is not registered."""
    response = api_client.post(login_url, {"email": "invaliduser@example.com", "password": "password123"})
    assert response.status_code == 400
    assert response.data["message"] == "Login failed"
    assert response.data["error"]["non_field_errors"] == ["Invalid email or password."]

@pytest.mark.django_db
def test_incorrect_password(api_client, login_url, create_user):
    """Test login with an incorrect password."""
    create_user(email="testuser@example.com", password="securepassword123")
    response = api_client.post(login_url, {"email": "testuser@example.com", "password": "wrongpassword"})
    assert response.status_code == 400
    assert response.data["message"] == "Login failed"
    assert response.data["error"]["non_field_errors"] == ["Invalid email or password."]


@pytest.mark.django_db
def test_missing_credentials(api_client, login_url):
    """Test login with missing email or password."""
    # Missing password
    response = api_client.post(login_url, {"email": "testuser@example.com"})
    assert response.status_code == 400
    assert response.data["message"] == "Login failed"
    assert "password" in response.data["error"]
    assert response.data["error"]["password"] == ["This field is required."]

    # Missing email
    response = api_client.post(login_url, {"password": "securepassword123"})
    assert response.status_code == 400
    assert response.data["message"] == "Login failed"
    assert "email" in response.data["error"]
    assert response.data["error"]["email"] == ["This field is required."]
