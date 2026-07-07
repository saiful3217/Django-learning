from django.shortcuts import render

# Create your views here.
def home(request):
    d={'author': 'Rahim', 'age':8  ,'l':[1,2,3,34,4,] }
    return render(request,'app_3/home.html',d)
