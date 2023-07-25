from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# def members(request):
#     return HttpResponse("1")

def members(request):
  template = loader.get_template('index1.html')
  return HttpResponse(template.render())