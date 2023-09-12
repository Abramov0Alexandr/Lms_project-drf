# LMS project (Learning Management System API)

В текущем проекте реализована разработка LMS-системы, в которой каждый желающий может размещать свои полезные материалы 
или курсы. Результатом создания проекта является бэкенд-сервер, который возвращает клиенту JSON-структуры.


## Стек технологий:
   - python
   - django
   - djangorestframework
   - djangorestframework-simplejwt
   - django-filters
   - psycopg2-binary
   - coverage
   - drf-yasg
   - django-cors-headers
   - eventlet 
   - celery
   - redis
   - django-celery-beat


## Установка
Прежде чем начать использовать LMS project, убедитесь, что у вас установлен 
интерпретатор Python (версия не ниже 3.9):

Клонируйте репозиторий с помощью следующей команды:
   ```bash
   git clone git@github.com:Abramov0Alexandr/Lms_project-drf.git
   ```

Перейдите в директорию проекта:
   ```bash
   cd Lms_project-drf
   ```

Установите зависимости с помощью Poetry:

   ```bash
   poetry install
   ```

Создайте и примените миграции для базы данных:

На ОС Windows:
   ```bash
   python manage.py migrate
   ```

На ОС Linux/Unix:

   ```bash
   python3 manage.py migrate
   ```

Запустите сервер:
   ```bash
   python manage.py runserver
   ```


## Возможности API
Healthy Habits Tracker предоставляет следующие возможности:

- Создание, редактирование, просмотр и удаление курсов.
- Создание, редактирование, просмотр и удаление уроков.
- Оформление платежей курсов или уроков.
- Авторизация пользователей с помощью JWT токена.
- Осуществление подписки на интересующие курсы.
- В случае обновления материалов курса, на которые подписан пользователем, 
происходит отправка уведомления на электронную почту.
- И многое другое!
   

## Документация
Healthy Habits Tracker предоставляет API для взаимодействия с приложением. Документацию к API вы можете найти здесь.<br>
http://127.0.0.1:8000/swagger/ <br>
http://127.0.0.1:8000/redoc/

## Лицензия
Healthy Habits Tracker распространяется под [MIT License](https://opensource.org/licenses/MIT).


## Контакты

Спасибо за использование Healthy Habits Tracker! Если у вас есть какие-либо вопросы или предложения, не стесняйтесь обращаться к нам.

Автор: [Alexandr Abramov <https://github.com/Abramov0Alexandr>]

Связь: [alexandr.abramovv@gmail.com]https://github.com/Abramov0Alexandr)

GitHub: [https://github.com/Abramov0Alexandr]