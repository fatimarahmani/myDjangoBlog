from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    return HttpResponse('about us')


def home(request):
    return HttpResponse('wellcome to Home')