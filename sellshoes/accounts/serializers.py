from rest_framework import serializers

from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, 
        write_only=True, 
        min_length=8
    )
    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, 
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'confirm_password']

    def validate_email(self, email):
        """Check if the email already exists."""
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email is already registered.")
        return email

    def validate(self, data):
        """Ensure password and confirm_password match."""
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords must match!"})
        return data

    def save(self, **kwargs):
        """Create and return a new user."""
        validated_data = self.validated_data
        validated_data.pop('confirm_password')  # Remove confirm_password from data
        user = User.objects.create_user(**validated_data)
        return user


# login Serializer 
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )

    def validate(self, data):
        """Validate email and password for login."""
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError("Both email and password are required.")

        user = authenticate(username=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid email or password.")

        data['user'] = user
        return data

