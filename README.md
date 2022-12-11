# Проект «API для Yatube»
## Описание
API социальной сети Yatube для публикации личных дневников.
### Функционал API Для Yatube:
* Просматривать, создавать новые, удалять и изменять посты.
* Просматривать и создавать группы.
* Комментировать, смотреть, удалять и обновлять комментарии.
* Просмотр подписок и подписываться на пользователя.
* Фильтровать по полям.

## Установка
### Клонируем репозиторий на локальную машину:

```
git clone https://github.com/vitek501/api_final_yatube.git
``` 

```
cd api_final_yatube
```

### Создаем виртуальное окружение:

```
python -m venv venv
```

### Устанавливаем зависимости:

```
pip install -r requirements.txt
```

### Создание и применение миграций:

```
python manage.py makemigrations
python manage.py migrate
```

### Запускаем django сервер:

```
python manage.py runserver
```

#### После запуск проекта,  по адресу `http://localhost:8000/redoc/` будет доступна документация.


## Примеры

Получение публикаций

``` 
curl --location --request GET 'http://127.0.0.1:8000/api/v1/posts/'
```
Получение JWT-токена
```
curl --location --request GET 'http://127.0.0.1:8000/api/v1/jwt/create/' \ 
--header 'Content-Type: application/json' \
--data-row '{"username": string, "password: string"}'
```