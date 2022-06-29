from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("this is first project")

def hai(request):
    return HttpResponse("this is 1st project")