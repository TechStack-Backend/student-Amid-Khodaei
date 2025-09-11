from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def hello(request):
    
    return HttpResponse("<h1>Hello Word Amid</h1>")