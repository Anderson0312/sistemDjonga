from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('plataforma/', include('plataforma.urls')),
    path('products/', include('products.urls')),
    path('custommers/', include('custommers.urls'))
]
