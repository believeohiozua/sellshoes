from rest_framework import serializers

from .models import Product, Category, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
        

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True)
    
    class Meta:
        model = Product
        fields = ['id', 'image', 'name', 'description', 'price', 'discount_price', 'quantity', 'category', 'tags', 'published']