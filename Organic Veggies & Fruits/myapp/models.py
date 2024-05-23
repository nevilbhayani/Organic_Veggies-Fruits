from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


class catagory(models.Model):
    cname=models.CharField(max_length=50)

    def __str__(self):
        return self.cname
    

class product(models.Model):
    catogary=models.ForeignKey(catagory,on_delete=models.SET_NULL,null=True)
    pname=models.CharField(max_length=30)
    pprice=models.IntegerField()
    qty=models.IntegerField()
    pimg=models.ImageField()

    def __str__(self):
        return self.pname

class cart(models.Model):
    userid=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    pid=models.ForeignKey(product,on_delete=models.SET_NULL,null=True)
    qty=models.IntegerField()

    def __str__(self):
        return self.pid.pname,self.pid.qty

class order(models.Model):
    userid=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    cname=models.CharField(max_length=30)
    pname=models.CharField(max_length=30)
    pprice=models.IntegerField()
    qty=models.IntegerField()
    pimg=models.ImageField()

    def __str__(self):
        return self.pname
    
    def __str__(self):
        return self.cname