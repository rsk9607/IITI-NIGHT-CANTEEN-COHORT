from django.urls import path
from . import views

urlpatterns = [
    path('',views.startup, name='startup'),
    path('menu/',views.Menu, name='menu')
]
