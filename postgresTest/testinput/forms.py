from django import forms
from .models import Product, Owner

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'description', 'image_url',]
        labels = { 'name': 'Product Name', 'price': 'Price', 'stock': 'Stock', 'description': 'Description', 'image_url': 'Image URL',}
        