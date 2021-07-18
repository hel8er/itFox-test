from .views import LoginAPIView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', LoginAPIView.as_view()),
    path('token/', obtain_auth_token)
]
