from django.urls import include, path

from partners import views


urlpatterns = [
    path('viewPartners/', views.viewPartners, name='viewPartners'),
    path('create_Partners/', views.create_Partners, name='create_Partners'),
    path('partners/<int:pk>/delete/', views.partner_delete.as_view(), name='partner_delete'),
]