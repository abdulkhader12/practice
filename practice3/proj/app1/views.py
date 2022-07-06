from django.shortcuts import render
from django.http import HttpRequest as req
from django.http import HttpResponse as res

def hello(e:req)->res:
    return res("<h1>Hello world</h1>")
# Create your views here.
