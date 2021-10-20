# Django_csv_googlemaps
```
A simple project with manager customers location using api from google maps to get latitude and longitude
```
## git clone
```py
git clone git@github.com:RegisSalesRA/Django_Csv_GoogleMaps.git
```
## virtual env

```py
python3 -m venv venv
source venv/bin/activate
```

## migrate db

```py
python3 manage.py makemigrations
python3 manage.py migrate
```

## Csv import command
```py
python manage.py import_customers customers.csv
```
## if you have docker-compose:
```py
use this command docker-compose up -d --build

install docker if you do not have https://docs.docker.com/compose/install/
```
## if you do not have docker-compose:
```py
or if you dont have you can use
use this command python3 manage.py runserver
```

## You can acesse customer api with swagger with this link
```py
http://127.0.0.1:8000/api/v1/swagger_v1
<img src="/readme/home.png" >
```

