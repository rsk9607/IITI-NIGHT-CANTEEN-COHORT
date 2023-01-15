from django.urls import path
from . import views

urlpatterns = [
    path('',views.night_canteen, name='night_canteen'),
    path('menu/',views.Menu, name='menu')
]
