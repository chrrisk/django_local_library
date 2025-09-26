from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("LocalLibrary home is alive ✅")

# Create your views here.
