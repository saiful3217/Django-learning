from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("This is Home Page")

def contact(request):
    return HttpResponse("This is Contact Page")
def index(request):
    return render(request,'index.html')
