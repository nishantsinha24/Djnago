from django.shortcuts import render

# Create your views here.

def index(request):
    tasks = ["foo" , "bar", "baz"]
    return render