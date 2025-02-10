from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import SignupSerializer, LoginSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema



# Create your views here.
class SignupView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING),
                "first_name": openapi.Schema(type=openapi.TYPE_STRING),
                "last_name": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
                "confirm_password": openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=["email", "first_name", "last_name", "password", "confirm_password"],
        ),
        responses={
            200: openapi.Response(
                description="Signup successful",
                examples={
                    "application/json": {
                        "message": "Signup successful",
                        "data": {
                            "id": 1,
                            "email": "user@example",
                            "first_name": "John",
                            "last_name": "Doe",
                        },
                        "error": None
                    }
                }
            ),
            400: openapi.Response(
                description="Signup failed",
                examples={
                    "application/json": {
                        "message": "Signup failed",
                        "data": None,
                        "error": {
                            "email": ["This field is required."],
                            "first_name": ["This field is required."],
                            "last_name": ["This field is required."],
                            "password": ["This field is required."],
                            "confirm_password": ["This field is required."]
                        }
                    }
                }
            ),
                            
        }
    )
    
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            send_mail(
                subject="Welcome to SellShoes",
                message=f"Thank you for signing up to SellShoes Inc. {user.first_name}. Thanks for signing up!",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=True,
            )
            return Response({
                "message": "Signup successful",
                "data": {
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                },
                "error": None
            }, status=status.HTTP_201_CREATED)
            
        return Response({
            "message": "Signup failed",
            "data": None,
            "error": serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)
            



# LoginView
class LoginView(APIView):
    # swagger decorator
    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            200: openapi.Response(
                description="Login successful",
                examples={
                    "application/json": {
                        "message": "Login successful",
                        "data": {
                            "access_token": "<JWT token>"
                        },
                        "error": None
                    }
                }
            ),
            400: openapi.Response(
                description="Login failed",
                examples={
                    "application/json": {
                        "message": "Login failed",
                        "data": None,
                        "error": "Invalid email or password."
                    }
                }
            ),
        }
    )
    # post method for login
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                "message": "Login successful",
                "data": {
                    "access_token": access_token,
                },
                "error": None
            }, status=status.HTTP_200_OK)

        return Response({
            "message": "Login failed",
            "data": None,
            "error": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

