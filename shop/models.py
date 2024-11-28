from django.db import models

# Create your models here.

class Products(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=10000)

class Order(models.Model):
    items = models.CharField(max_length=1000)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    postcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
