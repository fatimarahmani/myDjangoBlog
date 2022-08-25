from django.shortcuts import render
from . import models

def maqalat(request):
    x = models.Articles.objects.all().order_by('date')
    args = {'maqalat':x}
    return render(request, 'maqalat.html', args)
