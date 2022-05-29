from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index." )
def one(request):
    return HttpResponse("Hello, world. You're at the one")
def two(request):
    return HttpResponse("Hello, world. You're at the two.")