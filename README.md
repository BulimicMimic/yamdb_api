## API YamDB

### Описание:
v1.0 
Проект YaMDb собирает отзывы пользователей на произведения
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка»
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»)
Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв
Пользователи могут оставлять комментарии к отзывам
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи

### Использующиеся технологии:
```
Python 3.9
Django 3.2
DRF 3.12.4
JWT
```
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:COOLHax0r1337/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
### Примеры запросов: <br />
Получение списка всех произведений
```
GET http://127.0.0.1:8000/api/v1/titles/
Content-Type: application/json

{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "name": "string",
      "year": 0,
      "rating": 0,
      "description": "string",
      "genre": [
        {
          "name": "string",
          "slug": "string"
        }
      ],
      "category": {
        "name": "string",
        "slug": "string"
      }
    }
  ]
}
```
Добавление произведения
```
POST http://127.0.0.1:8000/api/v1/titles/
Content-Type: application/json

{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}

Response 201:

{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```
Создание пользователя
```
POST http://127.0.0.1:8000/api/v1/auth/signup/
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "string"
}

Response 200:
{
  "email": "string",
  "username": "string"
}
```

Получение списка всех отзывов
```
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
Content-Type: application/json

{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "text": "string",
      "author": "string",
      "score": 1,
      "pub_date": "2019-08-24T14:15:22Z"
    }
  ]
}
```
Авторы: <br />
[Кулхацкер](https://github.com/COOLHax0r1337) <br />
[Саня aka Давай тимлид оформляй проект!🤡](https://github.com/BulimicMimic) <br />
[Faceit Mirage + hookah enjoyer](https://github.com/talasov)
