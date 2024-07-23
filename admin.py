from django.contrib import admin
from api.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'retrieved_count')  

admin.site.register(Product, ProductAdmin)
