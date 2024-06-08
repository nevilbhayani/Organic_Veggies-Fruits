from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length=50)

    def _str_(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Catagory, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to='products/')

    def _str_(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    qty = models.IntegerField()

    def _str_(self):
        return f"{self.product.name} - {self.qty}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    qty = models.IntegerField()
    img = models.ImageField(upload_to='orders/')

    def _str_(self):
        return self.name


@receiver(post_delete, sender=Product)
def delete_product_image(sender, instance, **kwargs):
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)

@receiver(post_delete, sender=Order)
def delete_order_image(sender, instance, **kwargs):
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)