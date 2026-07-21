from django.shortcuts import render
from . forms import contactForm
# Create your views here.
def home(request):
    return render(request,'form_app/home.html')
def about(request):
    if request.method == "POST":
        name= request.POST.get('userName')
        email=request.POST.get('email')
        ratings=request.POST.get('ratings')
        return render(request,'form_app/about.html',{'name':name,'email':email, 'ratings':ratings })
    else:
        return render(request,'form_app/about.html')

def form(request):
    return render(request,'form_app/form.html')

def djangoForm(request):
    form=contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,'form_app/django_form.html',{'form': form})
    