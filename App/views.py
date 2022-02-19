# standard lib imports

# core django imports
from django.http import HttpResponse
from django.shortcuts import render

# third-party apps imports

# project apps import


def our_view(request, name):
    answer = f"""
    <html>
    <body>
    <p>Hello my friend {name}!!!!</p>
    </body>
    </html>
    """
    return HttpResponse(answer)
