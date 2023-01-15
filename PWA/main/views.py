from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def main(request):
    template = loader.get_template('menu.html')
    return HttpResponse(template.render())