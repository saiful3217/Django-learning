from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('This is first App home')
    return render(request,'first_app/home.html')

def courses(request):
    return HttpResponse('This is first App Courses page')
def contact(request):
    return HttpResponse('This is first App contact page')