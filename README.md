
## _Сервер авторизации и новостей_




## Запуск в Docker-контейнере




Скопировать репозиторий:

```sh
$ git clone https://github.com/hel8er/itfox-test.git
$ cd itfox-test
```

Отредактировать параметры подключения к БД в файле .env в корне проекта:

```
DB_ENGINE=postgresql # Тип БД
DB_DATABASE=dbase # Имя БД
DB_USER=user # Имя пользователя БД
DB_PASSWORD=passW0rd # Пароль БД
DB_PORT=5432 # Порт БД
DB_HOST=0.0.0.0 # Адрес БД
```
Далее собираем и запускаем контейнер:

```sh
$ docker-compose up --build
```
или ...
```sh
$ docker-compose up --build -d
```
... для запуска в режиме демона.


Для создания суперпользователя на запущеном контейнере:
```sh
$  docker exec -t -i itfox-test_testproject_1 python manage.py createsuperuser
```
На остановленном:
```sh
$  docker-compose run testproject python manage.py createsuperuser
```

## Точки входа

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Название | Путь | Демо |
| ------ | ------ | ------------|
| Сервер авторизации | /auth | [http://auth-news.bidbox.ru/auth/ |
| Сервер новостей | /news | http://auth-news.bidbox.ru/news/|
| Админка | /admin |  http://auth-news.bidbox.ru/admin/ |

_Тестовые учетные данные для демо:_
username: itfox
password: foxit
