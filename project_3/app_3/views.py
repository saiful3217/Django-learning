from django.shortcuts import render

# Create your views here.
def home(request):
    d={'author': 'Rahim', 'age':8  ,'l':[1,2,3,34,4,] }
    e={'author': 'aziz', 'age':70  ,'l':[91,29,38,34,44,] }
    return render(request,'app_3/home.html',{'d': d,'e':e})
