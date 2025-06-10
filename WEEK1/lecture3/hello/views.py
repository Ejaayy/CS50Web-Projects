from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def ej(request):
    return HttpResponse("Hello EJ!")

def rain(request):
    return HttpResponse("Hello Rain!")