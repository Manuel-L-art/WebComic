from django.shortcuts import render
from .models import *

def index(request):
    return render('index.html')