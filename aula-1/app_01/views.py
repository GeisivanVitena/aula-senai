from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def func1(request):
    return render(request, "app_01/index.html")

def func2(request):
    return render(request, "app_01/sobre.html")

def func3(request):
    return render(request, "app_01/ficha.html")