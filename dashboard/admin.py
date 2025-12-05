from django.contrib import admin
from .models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =('name', 'quantity', 'price', 'created_at')
    search_fields = ('name',)
    


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'staff', 'quantity', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('product__name', 'staff__username')
