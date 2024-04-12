from django.urls import path
from plataforma import views

urlpatterns = [
    path('index/', views.index, name='index'),
]