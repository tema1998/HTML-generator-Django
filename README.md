# Tailwind-generator Django application
It is a simple generator of HTML pages based on Tailwind CSS. You only need to select the required components and this application will build HTML page

## Frontend
[The second part](https://github.com/tema1998/NuxtJS-watch-shop) of this project is frontend based on Nuxt.JS and Tailwind.

## Installation on linux
First of all - clone repository.
Then create virtual environment:
```
python3 -m venv venv
```
Activate virtual environment:
```
source venv/bin/activate
```
You can install all the required dependencies by running
```
pip install -r requirements.txt
```

## Structure
It is a watch shop. It contains the following endpoints:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api/products/` | GET | READ | Get all products(with pagination)
`api/products/slug/` | GET | READ | Get product by slug
`api/products/?search=key` | GET | READ | Find products by key(with pagination)
`api/profile/` | GET | READ | Get info about user profile
`api/reviews/slug/` | GET | READ | Get reviews for product by product slug
`api/reviews/`| POST | CREATE | Create a review
`api/feedback/`| POST | CREATE | Write feedback to admin email
`api/register/`| POST | CREATE | Register
`api/token/`| POST | CREATE | Get "refresh" and "access" tokens
`api/refresh_token/`| POST | CREATE | Get new "access" token (refresh)
I'm working on this project and will be adding new features.


## Use
You can use second part of this project from my github. It is front-end for this project, based on Nuxt.js and Tailwind.
Or you can use Postman.

We have to start up Django's development server.
```
python manage.py runserver
```
