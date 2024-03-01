from rest_framework import serializers
from .models import Product, Review

class ProductListSerializer(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'mark', 'created_at']


class ProductDetailsSerializer(serializers.ModelSerializer):
    comments = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'comments']

