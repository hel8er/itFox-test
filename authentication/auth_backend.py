from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework.authtoken.models import Token


class CustomAuthentication(authentication.BaseAuthentication):
    """
    Реализация кастомной авторизации.
    Получаем учетные данные > возвращаем пользователя и токен
    """
    def authenticate(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username:
            return None

        user = User.objects.get(username=username)

        if user.check_password(password):

            token = Token.objects.get_or_create(user=user)
            print(token)
            return user, token



