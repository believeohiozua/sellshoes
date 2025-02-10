from rest_framework import generics 
from .models import Product
from .serializers import ProductSerializer

class ProductListAPIView(generics.ListAPIView):
    # List all products

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [] # Allow any user (authenticated or not) to access this endpoint
    
    
