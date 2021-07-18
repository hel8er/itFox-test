from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),  # Админ Панель
    path('auth/', obtain_auth_token),  # Ендпоинт получения токена
    path('news/', include('news.urls')),  # Ендпоинт получения списка новостей
]
urlpatterns += staticfiles_urlpatterns()