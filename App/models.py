from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)
    available = models.BooleanField(default=True)
    price = models.IntegerField(null=True)
    available_from = models.DateField(null=True)

    # wiele do jednego czyli z tabeli wiele robimy foreign key prowadzacy do tabeli one, przyklad:
    """
        class Company(models.Model):
            ..........
        class Phone(models.MOdel):
            person = blalblala
            company = models.FOreignKey(Company)
    """
    # realted_field = models.ForeignKey(<RElatedMOdel>, on_delete=models.CASCADE)
    # # jeden do jednego / w dowolonym
    # realted_field = models.OneToOneField(<RElatedMOdel>, on_delete=models.CASCADE)
    # # wiele do wielu
    # related  = models.ManyToManyField(<relatedModel>)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Discount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Topping(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField(default=3)


class Pizza(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField(default=10)
    toppings = models.ManyToManyField(to=Topping, through='MenuItem')


class MenuItem(models.Model):
    FINAL_TOUCHES = [
        ('Pep', 'Pepper'),
        ('Ruc', 'Ruccola'),
        ('Oil', 'Olive Oil'),
        ('Par', 'Parmiggiano'),
        ('Ore', 'Oregano'),
    ]
    pizza = models.ForeignKey(to=Pizza, on_delete=models.CASCADE)
    topping = models.ForeignKey(to=Topping, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField(default=30)
    final_touch = models.CharField(choices=FINAL_TOUCHES, max_length=20, default='Pep')
