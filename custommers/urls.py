from django.urls import include, path

from custommers import views


urlpatterns = [
    path('client/', views.create_custommmer, name='client'),
    path('clientview/', views.viewCustommer, name='clientview'),
    path('buscar/', views.buscar_Cliente, name='buscar_cliente'),
]