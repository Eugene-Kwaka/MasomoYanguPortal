# MasomoYanguPortal
A study portal to manage my studies. Contains notes and references for revisions

## Table of Contents
- [Background](#background)
- [Minimum Requirements](#minimum-requirements)
- [Quickstart](#quickstart)
- [Database SetUp](#database-setup)
- [Database Migration](#database-migration)
- [Deployment](#deployment)

## Background
This project is a student's study portal where they can track their Notes, Homework Assignments, and Todo lists. They can also research for references in Youtube, Wikipedia, Google Books and measurements.
The project applies Django's MVT(Model View Templates) architecture. It has a CRUD (Create Read Update Delete) application written with Function-Based Views (FBV) with focus on core fundamentals and whose use is easy to read, understand and implement.

## Minimum Requirements
This project supports Ubuntu Linux 20.04 and Windows OS with their previous stable releases. It has not been tested on Mac OS.

- [Python3](https://www.python.org/downloads/)
- [Django 3.2.3](https://www.djangoproject.com/)
- [Bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
- [PostgreSQL 14.2+](http://www.postgresql.org/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- [Git](https://git-scm.com/downloads)


## Quickstart
```bash
$ mkdir masomoyanguportal
$ cd masomoyanguportal
$ git init
$ git clone https://github.com/Eugene-Kwaka/MasomoYanguPortal.git
$ cd MasomoYanguPortal
$ sudo apt install python3-pip python3-django
$ sudo apt install python3-venv
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## Database Setup
``` settings.py
'ENGINE': 'django.db.backends.postgresql',
'NAME': ('DB_NAME'),
'USER': ('DB_USER'),
'PASSWORD': ('DB_PASSWORD'),
'HOST': ('DB_HOST'),
'PORT': ('DB_PORT')
```

## Database Migration
```bash
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

## Deployment
We'll deploy our application to Heroku. Heroku is a cloud hosting platform infrastructure with rapid scaling capabilities, offering flexible deployment services for all kinds of applications. Its ease of use makes it particularly suitable for fast development cycles.
```bash
$ git init
$ heroku login
$ heroku create <your_app_name>
$ heroku config:set DISABLE_COLLECTSTATIC=1
$ heroku config:set SECRET_KEY=<your_secret_key>
$ heroku config:set DATABASE_NAME=masomoyanguportal
$ heroku config:set DATABASE_USER=postgres
$ heroku config:set DEBUG_VALUE=True
$ heroku run python manage.py migrate
$ heroku open #the app should be served in your browser
```
