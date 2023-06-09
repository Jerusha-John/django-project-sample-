from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def home(request):
    products=Product.objects.all()
    return render(request,'home.html',{'products':products})
    # return HttpResponse("Hello World")

def contact(request):
    # return HttpResponse("This is my contact page")
    return render(request,'contact.html')

def about(request):
    # return HttpResponse("This is my About page")
    products=Product.objects.all()
    return render(request,'about.html',{'products':products})

def skills(request):
    # return HttpResponse("This is my portfolio page")
    return render(request,'portfolio.html')