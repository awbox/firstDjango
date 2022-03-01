# standard lib imports

# core django imports
from django.http import HttpResponse
from django.shortcuts import render

# third-party apps imports

# project apps import
from django.template.response import TemplateResponse

from App.models import Product, Pizza, Topping


def our_view(request, name):
    answer = f"""
    <html>
    <body>
    <p>Hello my friend {name}!!!!</p>
    </body>
    </html>
    """
    return HttpResponse(answer)


def our_view(request, name):
    product = Product.objects.get(id=3)
    answer = f"""
    <html>
    <body>
    <p>Hello my friend {name}!!!!</p>
    <p>You have just bought {product.name}</p>
    </body>
    </html>
    """
    return HttpResponse(answer)


def our_view(request):
    numery_lotto = [ 56, 6, 5, 87, 12, 45, ]
    context = {
        "name": "Maxi Dress",
        "klops": "zabawa",
        "lotto": numery_lotto,
    }

    return TemplateResponse(request, "base.html", context)


def jakikolwiek_widok(request):
    context = {}
    if request.method == 'GET':
        context["widoczne_url"] = request.GET.get("zmienna")
        context["widoczne_url2"] = request.GET.get("zmienna2")
        context["widoczne_url3"] = request.headers['User-Agent']
    return TemplateResponse(request, "base.html", context)


def order(request):
    cxt = {
        "pizzas": Pizza.objects.all(),
        "toppings": Topping.objects.all(),
    }
    return TemplateResponse(request, "order.html", cxt)


def saved_order(request):
    response = """
    <h1>Thank you for your order!</h1>
    """
    return HttpResponse(response)
