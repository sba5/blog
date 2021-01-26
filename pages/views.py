from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def index(req):
    return HttpResponse('hello world')