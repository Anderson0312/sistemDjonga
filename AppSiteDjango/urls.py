from django.urls import path


from.import views


urlpatterns = [
    path('',views.index, name='index'),
    path('signup/',views.create, name='signup'),
    path('signup/createUser/',views.createUser, name='createUser'),
    path('login/',views.login, name='login'),
]