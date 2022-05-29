from django.shortcuts import render


from django.http import HttpResponse

def helloasir(request):
    index = '<h1>Thi sis Asir </h1>'
    return HttpResponse(index)


# Create your views here.
