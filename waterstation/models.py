from django.db import models


# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    Email = models.CharField(max_length=40)
    Name = models.CharField(max_length=40)


class UserPurchase(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    ProductName = models.CharField(max_length=40)
    Quantity = models.CharField(max_length=40)
    Total = models.CharField(max_length=40)


class UserPurchaseHistory(models.Model):
    id = models.CharField(max_length=20, primary_key= True)
    ProductName = models.CharField(max_length=40)
    Quantity = models.CharField(max_length=40)
    Total = models.CharField(max_length=40)
    Status = models.CharField(max_length=40)


class Products(models.Model):
    ProductId = models.CharField(max_length=20, primary_key= True)
    ProductName = models.CharField(max_length=40)
    Price = models.CharField(max_length=40)

