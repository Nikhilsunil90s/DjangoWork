from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("<h1 style='text-align:center;color:red;'>Welcome To Home Page!</h1>")
    return render(request, 'home/homepage.html')#to send html files in response

