from django.db import models
from category.models import category
# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    description=models.CharField(max_length=500,blank=True)
    price=models.IntegerField()
    image=models.ImageField(upload_to='photos/products')
    stock=models.IntegerField()
    is_avaliable=models.BooleanField(default=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name