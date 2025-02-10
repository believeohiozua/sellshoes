from django.db import models
from accounts.models import CustomUser

# Base model for common fields
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Ensures this model won't create its own table


# Product
class Product(BaseModel):
    image = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)
    published = models.BooleanField(default=True)

# Category
class Category(BaseModel):
    name = models.CharField(max_length=100)

# Tag
class Tag(BaseModel):
    name = models.CharField(max_length=50)

# Cart
class Cart(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField('CartItem', related_name='carts')  # Explicit related_name
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    coupon = models.ForeignKey('Coupon', on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=10, decimal_places=2)

# CartItem
class CartItem(BaseModel):
    cart_item = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='cart_items')  # Explicit related_name
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

# ShippingAddress
class ShippingAddress(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=10)
    is_default = models.BooleanField()

# Bankcard
class Bankcard(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    card_holder = models.CharField(max_length=100)
    expiry_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)
    is_default = models.BooleanField()

# Coupon
class Coupon(BaseModel):
    code = models.CharField(max_length=20, unique=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2)

# Order
class Order(BaseModel):
    order_id = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ForeignKey('Cart', on_delete=models.CASCADE)
    shipping_address = models.ForeignKey('ShippingAddress', on_delete=models.CASCADE)
    bankcard = models.ForeignKey('Bankcard', on_delete=models.CASCADE)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2)
    total_products_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('paid', 'paid'), ('shipped', 'shipped'), ('delivered', 'delivered'), ('cancelled', 'cancelled')])
    tracking_number = models.CharField(max_length=20)
    
    