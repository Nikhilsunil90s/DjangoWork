from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def videoshome(request):
    return HttpResponse("<h1 style='text-align:center;color:cyan;'>Welcome To Videos Page!</h1>")
