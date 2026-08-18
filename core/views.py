from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def hello_world(request):
    name = "madhu"
    return render(request, "about.html",{"name":name})

def product(request):
    products = Product.objects.all()

    return render(request,"products.html",{"products":products})


