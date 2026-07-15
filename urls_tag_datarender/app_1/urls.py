from django.urls import path
from . import views

urlpatterns = [
    path('',views.load_data,name='home'),
    path('about/',views.about,name='about'),
]
