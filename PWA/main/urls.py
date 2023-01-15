from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.main, name='main'),
    path('menu/',views.Menu, name='menu')
]
