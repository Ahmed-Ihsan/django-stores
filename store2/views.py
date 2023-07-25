from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# def members(request):
#     return HttpResponse("2")

def members(request):
  template = loader.get_template('index2.html')
  return HttpResponse(template.render())