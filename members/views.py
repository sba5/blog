from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

# def index(req):
#     return HttpResponse("<h1>hello</h1>")


def index(req):
    return render(req, 'index.html')