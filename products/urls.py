from django.urls import include, path
from products import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastroProducts/', views.cadastroProducts, name='cadastroProducts'),
    path('buscar/', views.buscar_produto, name='buscar_produto'),
    path('viewProducts/', views.viewProducts, name='viewProducts'),
    path('produto/<int:pk>/delete/', views.ProdutoDeleteView.as_view(), name='produto_delete'),
    path('editar_produto/', views.editar_produto, name='editar_produto'),
    path('editar_produto/<int:produto_id>/', views.editar_produto, name='editar_produto'),
  
]