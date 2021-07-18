from .views import NewsAPIView
from django.urls import path

# Список новостей
urlpatterns = [
    path('', NewsAPIView.as_view()),
]
