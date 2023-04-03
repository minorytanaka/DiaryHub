### Описание:
Данный проект представляет собой REST API, написанный для проекта Django. Он позволяет взаимодействовать с базой данных и получать/отправлять данные в формате JSON.

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/minorytanaka/api_final_yatube.git
```
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python -m venv env
```
```
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```
### Примеры запросов:
 -   Получение публикаций: GET /api/v1/posts/
	 - Получить список всех публикаций. При указании параметров limit и offset выдача будет работать с пагинацией.
	 Пример ответа:
		 ```
				{
				  "count": 123,
				  "next": "http://api.example.org/accounts/?offset=400&limit=100",
				  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
				  "results": [
				    {
				      "id": 0,
				      "author": "string",
				      "text": "string",
				      "pub_date": "2021-10-14T20:41:29.648Z",
				      "image": "string",
				      "group": 0
				    }
				  ]
				}
		```

 -   Создание публикации: POST /api/v1/posts/
	 - Добавление новой публикации в коллекцию публикаций. Анонимные запросы
	   запрещены.
	   Пример запроса:
		```
		{
			"text": "string",
			"image": "string",
			"group": 0
		}
		```
		Пример ответа:
		```
		{
		    "id": 0,
		    "author": "string",
		    "text": "string",
		    "pub_date": "2019-08-24T14:15:22Z",
		    "image": "string",
		    "group": 0
		}
		```
 -   Получение определённой публикации: GET /api/v1/posts/{post_id}/
	 - Получение публикации по id.
	 Пример ответа:
		```
		{
		  "id": 0,
		  "author": "string",
		  "text": "string",
		  "pub_date": "2019-08-24T14:15:22Z",
		  "image": "string",
		  "group": 0
		}
		```
 -  Обновление публикации: PUT /api/v1/posts/{post_id}/
	 - Обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены.
	 Пример запроса:
		```
		{
		  "text": "string",
		  "image": "string",
		  "group": 0
		}
		```
		Пример ответа:
		```
		{
		  "id": 0,
		  "author": "string",
		  "text": "string",
		  "pub_date": "2019-08-24T14:15:22Z",
		  "image": "string",
		  "group": 0
		}
		```
 -   Частичное обновление публикации: PATCH /api/v1/posts/{id}/
	 - Частичное обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены.
	 Пример запроса:
		```
		{
		  "text": "string",
		  "image": "string",
		  "group": 0
		}
		```
		Пример ответа:
		```
		{
		  "id": 0,
		  "author": "string",
		  "text": "string",
		  "pub_date": "2019-08-24T14:15:22Z",
		  "image": "string",
		  "group": 0
		}
		```
		
 -   Удаление публикации: DELETE /api/v1/posts/{post_id}/
	 - Удаление публикации по id. Удалить публикацию может только автор публикации. Анонимные запросы запрещены.
 -   Получение комментариев: GET /api/v1/posts/{post_id}/comments/
	 - Получение всех комментариев к публикации.
	 Пример ответа:
		```
		[
		  {
		    "id": 0,
		    "author": "string",
		    "text": "string",
		    "created": "2019-08-24T14:15:22Z",
		    "post": 0
		  }
		]
		```
 -   Добавление комментария: POST /api/v1/posts/{post_id}/comments/
	 - Добавление нового комментария к публикации. Анонимные запросы запрещены.
	 Пример запроса:
		```
		{
		  "text": "string"
		}
		```
		Пример ответа:
		```
		{
		  "id": 0,
		  "author": "string",
		  "text": "string",
		  "created": "2019-08-24T14:15:22Z",
		  "post": 0
		}
		```
 -   Получение комментария: GET /api/v1/posts/{post_id}/comments/{comment_id}/
	 - Получение комментария к публикации по id.
	 Пример ответа:
		```
		{
		  "id": 0,
		  "author": "string",
		  "text": "string",
		  "created": "2019-08-24T14:15:22Z",
		  "post": 0
		}
		```
 -   Обновление комментария: PUT /api/v1/posts/{post_id}/comments/{comment_id}/
		- Обновление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы запрещены.
		 Пример запроса:
		```
		{
		  "text": "string"
		}
		```
		Пример ответа:
		```
		{
		  "id": 0,
		  "author": "string",
		  "text": "string",
		  "created": "2019-08-24T14:15:22Z",
		  "post": 0
		}
		```
 -    Удаление комментария: DELETE /api/v1/posts/{post_id}/comments/{comment_id}/
		- Удаление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы запрещены.
 -   Получение всех групп: GET /api/v1/groups/
	 - Получение списка доступных сообществ.
	 Пример ответа:
		```
		[
		  {
		    "id": 0,
		    "title": "string",
		    "slug": "string",
		    "description": "string"
		  }
		]
		```
 -   Информация о сообществе: GET /api/v1/groups/{group_id}/
	 - Получение информации о сообществе по id.
	 Пример ответа:
		```
		{
		  "id": 0,
		  "title": "string",
		  "slug": "string",
		  "description": "string"
		}
		```
 -   Подписки: GET /api/v1/follow/
	 - Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены.
	 Пример ответа:
		```
		[
		  {
		    "user": "string",
		    "following": "string"
		  }
		]
		```
 -   Подписка: POST /api/v1/follow/
	 - Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены.
	 Пример запроса:
		```
		{
		  "following": "string"
		}
		```
		Пример ответа:
		```
		{
		  "user": "string",
		  "following": "string"
		}
		```
-  Получить JWT-токен: POST /api/v1/jwt/create/
	- Получение JWT-токена.
		 Пример запроса:
		```
		{
		  "username": "string",
		  "password": "string"
		}
		```
		Пример ответа:
		```
		{
		  "refresh": "string",
		  "access": "string"
		}
		```
-  Обновить JWT-токен: POST /api/v1/jwt/refresh/
	- Обновление JWT-токена.
		 Пример запроса:
		```
		{
		  "refresh": "string"
		}
		```
		Пример ответа:
		```
		{
		  "access": "string"
		}
		```
-  Проверить JWT-токен: POST /api/v1/jwt/verify/
	- Проверка JWT-токена.
		 Пример запроса:
		```
		{
		  "token": "string"
		}
		```
### Технологии
API написан на языке Python с использованием библиотеки Django REST framework. В качестве базы данных используется SQLite.