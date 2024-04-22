from django.urls import include, path
from products import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastroProducts/', views.cadastroProducts, name='cadastroProducts'),
    path('viewProducts/', views.viewProducts, name='viewProducts'),
    path('buscar/', views.buscar_produto, name='buscar_produto'),
  
]