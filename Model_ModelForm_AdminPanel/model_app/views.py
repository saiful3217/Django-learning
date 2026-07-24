from django.shortcuts import render,redirect
from . import models
# Create your views here.
def home(request):
    data= models.Student.objects.all()
    print(data)
    return render(request,'home.html',{'datas': data})


def delete_student(request,roll):
    std=models.Student.objects.get(pk=roll)
    std.delete()
    return redirect('homepage')
    
