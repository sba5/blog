from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.

def photo(req):
    return render(req, 'photo.html') 