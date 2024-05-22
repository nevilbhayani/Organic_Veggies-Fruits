from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from decimal import Decimal

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def _str_(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def _str_(self) -> str:
        return self.name

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='cart_items')
    quantity = models.PositiveIntegerField()

    def _str_(self) -> str:
        return f"{self.quantity} of {self.product.name}"

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='orders')
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.total is None:
            self.total = self.quantity * self.product.price
        if self.amount == 0:
            self.amount = self.total
        super().save(*args, **kwargs)

    def _str_(self) -> str:
        return f"Order of {self.quantity} {self.product.name}(s) on {self.date}"