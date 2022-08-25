from datetime import date
from pyexpat import model
from turtle import title
from django.db import models

class Articles(models.Model):
    title= models.CharField(max_length= 100)
    slug= models.SlugField()
    body= models.TextField()
    date= models.DateTimeField(auto_now_add= True)
    #ax
    #author

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:20]+ ' ...'