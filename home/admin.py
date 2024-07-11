from django.contrib import admin
from .models import User, Product, Image
# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ["status"]
    inlines = [
        ImageInline,
    ]

class ProductInline(admin.TabularInline):
    model = Product
    exclude = ["description", "price", "status"]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]