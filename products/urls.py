from django.urls import include, path
from products import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastroProducts/', views.cadastroProducts, name='cadastroProducts'),
    # path('profile/', views.profile, name='profile'),
  
]