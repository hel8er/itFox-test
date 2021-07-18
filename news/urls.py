from .views import NewsAPIView
from django.urls import path


urlpatterns = [
    path('', NewsAPIView.as_view()),
]
