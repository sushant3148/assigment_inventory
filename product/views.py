from django.http import JsonResponse, HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Product
import json
from rest_framework import generics 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class allProductList(View):
    def get(self, request):
        p = Product.objects.all()
        print(p)
        products = list(p.values())
        return JsonResponse(products, safe=False)
        
@method_decorator(csrf_exempt, name='dispatch')
class allProductDetail(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return JsonResponse({
            'id': product.id,
            'name': product.name,
            'category': product.category,
            'price': product.price,
        })

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        data = json.loads(request.body)
        print(data)
        for key, value in data.items():
            setattr(product, key, value)
        product.save()
        return JsonResponse({
            'id': product.id,
            'name': product.name,
            'category': product.category,
            'price': product.price,
        })

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product_name = product.name  
        product.delete()
        return JsonResponse({'message': f'"{product_name}" successfully deleted'}, status=204)
