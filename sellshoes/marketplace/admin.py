from django.contrib import admin
from marketplace.models import Product, Category, Tag, Cart, CartItem, ShippingAddress, Bankcard, Coupon, Order

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(ShippingAddress)
admin.site.register(Bankcard)
admin.site.register(Coupon)
admin.site.register(Order)