from django.shortcuts import render
from django.http import HttpResponse

def amar (request):
    return HttpResponse ('<h1><marqee> hlo pranthaman </marquee></h1>')

# Create your views here.
