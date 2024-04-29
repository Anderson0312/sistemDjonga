from django.urls import include, path

from custommers import views


urlpatterns = [
    path('client/', views.create_custommmer, name='client'),
    
]