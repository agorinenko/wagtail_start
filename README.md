# Типовой шаблон Django проекта
## Описание
* [Административный интерфейс](http://localhost/admin/)
## Первый запуск и развертывание
### Настройка переменных окружения
Создать .env файл на основе ``.env.example``
### Запуск приложения
#### В dev режиме
``` bash
docker-compose -f docker-compose.dev.yml up -d --build --force-recreate
```
#### В prod режиме
``` bash
docker-compose up -d --build --force-recreate
```
#### В изолированном режиме
``` bash
docker-compose -f docker-compose.self.yml up -d --build --force-recreate
```
## Установка зависимостей для dev режима
``` bash
pip install -r requirements.dev.txt
```
## Для работы
### Создание администратора
``` bash
python manage.py createsuperuser
```
### Миграции
Создание, если нужно
``` bash
python manage.py makemigrations
```
Накатываем
``` bash
python manage.py migrate
```
Просмотр миграций
``` bash
python manage.py showmigrations
```
Откатываем все миграции приложения
``` bash
python manage.py migrate web_app zero
```
или возвращаемся к 0001_initial
``` bash
python manage.py migrate web_app 0001_initial
```
Создание пустой миграции
``` bash
python manage.py makemigrations --empty web_app
```
### Создание приложения
``` bash
python manage.py startapp app_name
```
### Запуск тестов из консоли
``` bash
pytest --cov=web_app
```
### Запуск pylint из консоли
``` bash
pylint ./web_app --load-plugins pylint_django --django-settings-module=web_app.settings
```
