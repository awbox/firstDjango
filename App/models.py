from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)
    available = models.BooleanField(default=True)
    price = models.IntegerField(null=True)
    available_from = models.DateField(null=True)
