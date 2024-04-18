from django.urls import path
from plataforma import views

urlpatterns = [
    path('', views.index, name='index'),
]