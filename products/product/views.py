from django.shortcuts import render
from django.views import View
from .serializer import ProductSerializer
from .data import products
from django.http import JsonResponse

# Create your views here.


class ProductList(View):
    def get(self, request):
        serialized_product = ProductSerializer(products, many=True).data
        return JsonResponse(serialized_product, safe=False)
