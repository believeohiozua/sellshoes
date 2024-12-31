from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SignupSerializer

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
        responses={201: "Signup successful", 400: "Signup failed"},
    )
    
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            send_mail(
                subject="Welcome to SellShoes",
                message=f"Thank you for signing up to SellShoes Inc. {user.first_name}.",
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
            
