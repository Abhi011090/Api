from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()  # Corrected spelling
    price = models.DecimalField(max_digits=10, decimal_places=2)

class ProductView(models.Model):  
    product = models.ForeignKey(Product, related_name='views', on_delete=models.CASCADE)  
    view_at = models.DateTimeField(auto_now_add=True)
