from django.db import models

# Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=100)

# class Product(models.Model):
#     product_name = models.TextField()
#     description = models.TextField()
    # image = models.ImageField(upload_to='products')
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    # owner = models.ForeignKey("User", on_delete=models.CASCADE)
    
    # #  Optional
    # def __str__(self):
    #     return self.product_name
    
class Records(models.Model):
    region = models.TextField(max_length=100)
    country = models.TextField(max_length=100)
    item_type = models.TextField(max_length=100)
    sales_channel = models.TextField(max_length=100)
    
    #  Optional
    def __str__(self):
        return self.item_type