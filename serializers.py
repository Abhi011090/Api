from rest_framework import serializers
from api.models import Product,ProductView

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price'] 