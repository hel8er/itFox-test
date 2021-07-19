
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
_____
или.для запуска в режиме демона:
```sh
$ docker-compose up --build -d
```
____

Создаем админа:
|на запущеном контейнере|На остановленном:|
| ------ | ------ |
|```$ docker exec -t -i itfox-test_testproject_1 python manage.py createsuperuser```|```$ docker-compose run testproject python manage.py createsuperuser```|
___
Генерируем и применяем миграции:
|на запущеном контейнере|На остановленном:|
| ------ | ------ |
|```$ docker exec -t -i itfox-test_testproject_1 python manage.py makemigrations```|```$ docker-compose run testproject python manage.py makemigrations```|
|```$ docker exec -t -i itfox-test_testproject_1 python manage.py migrate```|```$ docker-compose run testproject python manage.py migrate```|
___
## Точки входа


| Название | Путь | Демо |
| ------ | ------ | ------------|
| Сервер авторизации | /auth | http://auth-news.bidbox.ru/auth/ |
| Сервер новостей | /news | http://auth-news.bidbox.ru/news/|
| Админка | /admin |  http://auth-news.bidbox.ru/admin/ |
____
_Тестовые учетные данные для демо:_
|username|password|
| ------ | ------ |
|itfox|!TF0X|
