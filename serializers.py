from rest_framework import serializers
from api.models import Product,ProductView

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price')
class ProductViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductView
        fields = ('id','product','view_count')
