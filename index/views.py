from email import message
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):

    mess = '<h1> tHis is Index</h1>'
    return HttpResponse(mess)

