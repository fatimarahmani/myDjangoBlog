from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path('', views.maqalat, name="list"),
    path('<slug>', views.showSlug, name="detail"),
]
