from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('profile/', views.profile, name='profile'),
    path('plataforma/', views.plataforma, name='plataforma'),
]