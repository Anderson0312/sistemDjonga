from django.urls import path
from accounts import views

urlpatterns = {
    path('', views.login, name='login'),
    path('', views.register, name='register'),
}