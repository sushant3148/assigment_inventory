from django.urls import path
from .views import allProductList, allProductDetail

urlpatterns = [
    path('products/', allProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', allProductDetail.as_view(), name='product-detail'),
]
