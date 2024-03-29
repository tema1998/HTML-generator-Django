# HTML-generator Django application
It is a simple generator of HTML pages based on Tailwind CSS components. You only need to select the required components and this application will build HTML page for your project.

## Tailwind
This is not a commercial project. All components used in the project are taken from the next sites: \
[flowbite.com](https://flowbite.com/) \
[tw-elements.com](https://tw-elements.com/) 

## Screenshot
<image align="center" src="tailwind_generator/static/img/screen.png" alt="">

## Functions
HTML page creation is implemented using the library BeautifulSoup4.

Functions |
-- |
`Project repository` |
`Choose header` |
`Choose footer` |
`Add sign in form` |
`Add sign up form` |
`Create page` |
`Download HTML file` |
`Sign Up/ Sign In/ Log out` |
`Add components through admin panel.` |

Other HTML components will be added later.

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
Install all the required dependencies by running
```
pip install -r requirements.txt
```

Migrate:
```
python manage.py makemigrations
```

Then start up Django's development server.
```
python manage.py runserver
```