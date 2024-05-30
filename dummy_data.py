import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory.settings')
django.setup()

from product.models import Product
from pymongo import MongoClient

# MONGO_URI = 'mongodb://mongo:27018/'
# client = MongoClient(MONGO_URI)
# db = client['inventory']

def dummy_data():
    products = [
        {'name': 'harpick', 'category': 'household', 'price': 37.00},
        {'name': 'magiie', 'category': 'food', 'price': 14.00},
        {'name': 'tea', 'category': 'food', 'price': 67.99},
        {'name': 'cold drink', 'category': 'drink', 'price': 39.50},
        {'name': 'wheat', 'category': 'food', 'price': 25.99},
    ]
    

    for product_data in products:
        product, created = Product.objects.get_or_create(
            name=product_data['name'],
            defaults={
                'category': product_data['category'],
                'price': product_data['price'],
            }
        )
        if created:
            print(f"Successfully added {product.name}")
        else:
            print(f"{product.name} already exists")

if __name__ == '__main__':
    dummy_data()
