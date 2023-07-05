from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello !")

def mohan(request):
    return HttpResponse("Hello, Mohan")

def sohan(request):
    return HttpResponse("Helo, Sohhan")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()} !")

