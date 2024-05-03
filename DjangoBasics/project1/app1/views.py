from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def SignUpLoader(request):
    template = loader.get_template('BS5.html')
    return HttpResponse(template.render())

def ColorLoader(request):
    template = loader.get_template('DOM.html')
    return HttpResponse(template.render())