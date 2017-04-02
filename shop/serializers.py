from rest_framework import serializers
from shop import models as shop_models


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = shop_models.Product
        fields = '__all__'


class ProductInCartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = shop_models.ProductInCart
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    products = ProductInCartSerializer(many=True, read_only=True, source='productincart_set')

    class Meta:
        model = shop_models.Cart
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Order
        fields = ('product', 'cart', )

