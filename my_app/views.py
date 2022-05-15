from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse("Hello World!")


def friends(requst):
    return HttpResponse("There is no friends!")
