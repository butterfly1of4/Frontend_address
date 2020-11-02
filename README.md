# The test front end

## Requirements for build: Python, Django, Pipenv, postgreSQL

Dependencies:
pipenv
django
postgreSQL

### To install pipenv:
`brew install pipenv`
### To install django:
`pipenv install django`
**To install the library connecting Django to SQL:
`pipenv install psycopg2-binary`
**_NOTE: THE PERIOD AT THE END OF THE STRING MUST BE THERE TO WORK_**
### To initiate a new project:
`pipenv run django-admin startproject frontend_test .`
`pipenv install django-extensions`


## Setup:
Get into the Django environment you created:
`pipenv shell`
Create app:
`$ django-admin startapp book`
OR- if manage.py is in your current directory
`python3 manage.py`

Database setup:
In a seperate console, type:
`psql -d postgres`
to connect you to postgres to enable you to create or access the database. If you are creating a new database:
`CREATE DATABASE name;`
`CREATE USER tunruser WITH PASSWORD 'name';`
`GRANT ALL PRIVILEGES ON DATABASE tunr TO nameuser;`
`\q`
My database is named: frontend;

In 'frontend_test/settings.py', updated the database using this example:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '_user',
        'PASSWORD': '',
        'HOST': 'localhost'
    }
}
```

In the same file, add:
'contacts' and 'django_extensions'
 to Installed_Apps

To migrate the schemas/models to use the database:
```python3 manage.py makemigrations```
```python3 manage.py migrate```

After the Modesl have been created, add the models and site to admin.py

To seed database still inside virtual environment, run:
`python3 manage.py loaddata frontend.json`

To view the database, go to:
localhost:8000/admin
Create a superuser: 
```python3 manage.py createsuperuser```

To run the server:
```python3 manage.py runserver```

## After adding a 'templates' folder to the file holding the database (in this case 'address'):

### Django REST framework 
In the virtual director (pipenv shell) run:
```pipenv install djangorestframework```
and add to the INSTALLED_APPS section of the settings.py folder. 

### CORS
