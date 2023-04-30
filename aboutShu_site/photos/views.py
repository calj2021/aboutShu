from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    return render(request, 'photos/home.html')

def index(request):

    return render(request, 'photos/index.html')

def flower(request):

    return render(request, 'photos/flower.html')

def landscape(request):

    return render(request, 'photos/landscape.html')

def city(request):

    return render(request, 'photos/city.html')

def lighting(request):

    return render(request, 'photos/lighting.html')