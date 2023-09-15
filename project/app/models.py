from django.db import models
from django.contrib.auth.models import User
from .managers import Mymanager

class earbud(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField(upload_to='Downloads')
    price=models.FloatField()
    quantity=models.IntegerField()
    available=models.BooleanField(default=True)
    desc=models.TextField()
    objects=models.Manager()
    products=Mymanager()

class contact(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    message=models.CharField(max_length=250)

class transaction(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    cat=models.CharField(max_length=50)
    cat_id=models.IntegerField()
    purchased_quan=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
     

class ItemModel(models.Model):
    name = models.CharField(max_length = 100)
    amount = models.IntegerField()
    order_id = models.CharField(max_length = 100)
    razorpay_payment_id = models.CharField(max_length = 100,blank=True)
    paid = models.BooleanField(default=False)



    def __str__(self):
        return self.name+str(self.id)

    # ecommproject
    # project123

# Create your models here.