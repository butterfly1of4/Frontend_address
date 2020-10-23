CREATE DATABASE address;
CREATE USER addressuser WITH PASSWORD 'address';
GRANT ALL PRIVILEGES ON DATABASE address TO addressuser;

--instructions:

-- if you already have an address database run:
--DROP DATABASE address;
--DROP USER addressuser;

--Then, to create address database in psql run inside top level api directory:
--psql -U postgres -f settings.sql

--In your virtual environment (pipenv shell) translate the models into the schema for our database, run:
--python3 manage.py makemigrations
--python3 manage.py migrate

--To seed database still inside virtual environment, run:
--python3 manage.py loaddata address.json

--to view database in localhost:8000/admin create superuser:
--python3 manage.py createsuperuser

--to run the server:
--python3 manage.py runserver

--API!!!!!!

--to view as api with crud use:
--localhost:8000/address 
