from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),  # Админ Панель
    path('auth/', obtain_auth_token),  # Ендпоинт получения токена
    path('news/', include('news.urls')),  # Ендпоинт получения списка новостей
]
