from django.shortcuts import render
from . forms import contactForm, StudentData
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
    if request.method=='POST':
        form=contactForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
        #     upload_file=form.cleaned_data['file']
        #     with open ('./form_app/upload/'+ upload_file.name , 'wb+' ) as destination:
        #         for chunk in upload_file.chunks():
        #             destination.write(chunk)
    else:
        form=contactForm()

    return render(request,'form_app/django_form.html',{'form': form})

    
def StudentForm(request):
    if request.method=='POST':
        form=StudentData(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form=StudentData()

    return render(request,'form_app/django_form.html',{'form': form})