from django.urls import include, path
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('profile/', views.profile, name='profile'),
    path('users/', views.users, name='users'),
    # path('logout/', views.logout, name='logout'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout')
]