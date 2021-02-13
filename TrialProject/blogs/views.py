from django.shortcuts import render
from django.http import HttpResponse
from .models import Categorie , BlogPost
# Create your views here.
def blogHome(request):
    results = BlogPost.objects.all()
    print(results)
    return render(request , "blogs/blogHome.html" , {'blogs' : results})