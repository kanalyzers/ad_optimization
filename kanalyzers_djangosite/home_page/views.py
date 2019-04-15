from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Ryan Smells like farts</h1>')

# Create your views here.
