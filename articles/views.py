from django.shortcuts import render,HttpResponse
from . import models
from django.contrib.auth.decorators import login_required

def maqalat(request):
    x = models.Articles.objects.all().order_by('-date')
    args = {'maqalat':x}
    return render(request, 'maqalat.html', args)

def showSlug(request, slug):
    y = models.Articles.objects.get(slug = slug)
    args = {'details':y}
    return render(request, 'details.html',args)

@login_required(login_url= "/accounts/login")
def creat_article(request):
    return render (request, 'creat_article.html')