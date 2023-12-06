from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    address = models.CharField(max_length=100, verbose_name='address')

    def __str__(self):
        return self.name


class User(models.Model):
    name_user = models.CharField(max_length=100, verbose_name='name')
    email = models.EmailField(verbose_name='email')
    message = models.TextField()

    def __str__(self):
        return self.name_user

class Product(models.Model):
    name_product = models.CharField(max_length=100, verbose_name='name_product')
    price = models.FloatField()