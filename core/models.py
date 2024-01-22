from django.contrib.auth.models import User
from django.db import models
import ast


class ListField(models.TextField):
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        if isinstance(value, str):
            return value.split(',')

    def to_python(self, value):
        if not value:
            value = []
        if isinstance(value, list):
            return value
        if isinstance(value, str):
            return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value
        if value is not None and isinstance(value, str):
            return value
        if isinstance(value, list):
            return ','.join(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)


class Header(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='header_images')
    html = models.FileField(upload_to='header_html')

    def __str__(self):
        return self.name

    @classmethod
    def get_description(cls):
        return ("The website header is the first thing your website visitors are going to see when they land on your "
                "website's homepage. It is typically a combination of text and imagery that help visitors get an idea "
                "of what your business does from first glance.")


class Footer(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='footer_images')
    html = models.FileField(upload_to='footer_html')

    def __str__(self):
        return self.name

    @classmethod
    def get_description(cls):
        return ('The website footer is found at the bottom of your site pages. It typically includes important '
                'information such as a copyright notice, a disclaimer, or a few links to relevant resources.')


class Signup(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='signup_images')
    html = models.FileField(upload_to='signup_html')

    def __str__(self):
        return self.name

    @classmethod
    def get_description(cls):
        return ('A signup page (also known as a registration page) enables users and organizations to independently '
                'register and gain access to your system. ')


class Signin(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='signin_images')
    html = models.FileField(upload_to='signin_html')

    def __str__(self):
        return self.name

    @classmethod
    def get_description(cls):
        return ('A login page is a webpage that allows a user to gain access to a website or application by entering '
                'their credentials, such as a username and password. The login page typically includes fields for '
                'entering these credentials and a submit button for sending the information to the server for '
                'verification. ')


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=30, blank=True, null=True)
    default_processed_components = ListField(default=['header', 'footer'])
    header = models.ForeignKey(Header, on_delete=models.CASCADE, blank=True, null=True)
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, blank=True, null=True)
    signin = models.ForeignKey(Signin, on_delete=models.CASCADE, blank=True, null=True)
    signup = models.ForeignKey(Signup, on_delete=models.CASCADE, blank=True, null=True)
    result_html = models.FileField(blank=True, null=True)
