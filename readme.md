СТТ внутренний портал
=========================
О проекте
----------

Информационный ресурс предназначен для систематизации и централизованного доступа сотрудников к информации, связанной с функционированием предприятия, организацией рабочего процесса, проводимым мероприятиям, применяемым технологиям.

Установка
----------
Клонировать репозиторий

    git clone https://github.com/abirukov/stt_portal.git
    cd stt_portal

Создать виртуальное окружение

    python3.12 -m venv venv

Активировать виртуальное окружение
    
    source venv/bin/activate

Установить poetry

    pip install poetry

Установить зависимости python

    poetry install --without dev --sync

Так же для корректной работы проекта потребуется дополнительное ПО

    sudo apt-get install libsasl2-dev libldap2-dev libssl-dev
    sudo apt install libreoffice

Затем прописываем конфигурацию в файл .env в корне проекта, пример содержимого:

    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=postgres
    DB_HOST=localhost
    DB_PORT=5432
    DB_USER=postgres
    DB_PASSWORD=postgres
    DJANGO_SECRET_KEY="django-secret-key"
    ALLOWED_HOSTS='["0.0.0.0", "127.0.0.1", "localhost"]'


Затем запускаем миграции

    python manage.py migrate


Запускаем проект
    
    python manage.py runserver
