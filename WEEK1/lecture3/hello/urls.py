from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"), #when you have a URL String like name, you call greet function
    path("ej", views.ej, name = "ej"), #opens the function inside views like methods
    path("rain", views.rain, name = "rain")
    
]