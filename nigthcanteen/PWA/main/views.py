from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import menu

# Create your views here.

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def Menu(request):
    my_menu = menu.objects.all().values()
    template = loader.get_template('menu.html')
    context = {
        'my_menu' : my_menu,
    }
    return HttpResponse(template.render(context,request))