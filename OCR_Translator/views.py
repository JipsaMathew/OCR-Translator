from django.shortcuts import render
from . import service

# Create your views here.

def index(request):
    return render(request, 'OCR_Translator/index.html')




