from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path('', views.maqalat, name= "list"),
    path('create', views.creat_article, name= "create"),
    path('<slug>', views.showSlug, name= "detail"),
]
