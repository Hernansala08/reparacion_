from django.shortcuts import render
from .models import Celular, Laptop, PC

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def more(request):
    return render(request, 'core/more.html')

def celulares(request):
    Cel = Celular.objects.all()
    return render(request, 'core/more.html',{'Celulares':Cel})

def laptops(request):
    Lap = Laptop.objects.all()
    return render(request, 'core/more.html',{'Laptops':Lap})

def pcs(request):
    Pc = PC.objects.all()
    return render(request, 'core/more.html',{'PCs':Pc})