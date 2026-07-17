from django.urls import path
from . import views
urlpatterns = [
    path('iteams/',views.items,name='iteams'),
]
