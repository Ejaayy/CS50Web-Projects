from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def ej(request):
    return HttpResponse("Hello EJ!")

def rain(request):
    return HttpResponse("Hello Rain!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")