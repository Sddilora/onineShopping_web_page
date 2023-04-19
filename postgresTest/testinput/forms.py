from django import forms
from .models import Product, Owner

class ProductForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('women', 'Women'),
        ('men', 'Men'),
        ('kids-baby', 'Kids & Baby'),
        ('home', 'Home'),
        ('bed-bath', 'Bed & Bath'),
        ('jewelery', 'Jewelery'),
        ('electronics', 'Electronics'),
        ('arts-crafts', 'Arts & Crafts'),
    ]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Category')

    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'description', 'image_url', 'category']
        labels = { 'name': 'Product Name', 'price': 'Price', 'stock': 'Stock', 'description': 'Description', 'image_url': 'Image URL'}
        