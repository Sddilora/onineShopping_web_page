from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
class Product(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField()
    image_url = models.CharField(max_length=2083)
