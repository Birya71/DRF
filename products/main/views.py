from django.shortcuts import render, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer
from .models import Product, Review


@api_view(['GET'])
def products_list_view(request):
    all_product = Product.objects.all()
    ser_product = ProductListSerializer(all_product, many=True)
    return Response(ser_product.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try:
            prod = Product.objects.get(id=product_id)
            ser_prod = ProductDetailsSerializer(instance=prod)
            return Response(ser_prod.data)
        except Product.DoesNotExist:
            raise Http404


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        pass
