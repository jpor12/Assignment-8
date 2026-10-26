from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello, World! This is my first Django app.</h1>")

def about(request):
    return HttpResponse("<h1>About Us\nThis is the about page of my Django app.</h1>")

def information(request):
    return HttpResponse("<h1>Information\nThis is the information page for my Django app.</h1>")