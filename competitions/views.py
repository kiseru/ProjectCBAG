from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Hello! It is a project for competition for the best academic group.")
