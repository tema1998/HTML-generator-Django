from django.contrib.auth.models import User
from django.db import models


class Header(models.Model):
    name = models.CharField(max_length=100)
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
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='footer_images')
    html = models.FileField(upload_to='footer_html')

    def __str__(self):
        return self.name

    @classmethod
    def get_description(cls):
        return ('The website footer is found at the bottom of your site pages. It typically includes important '
                'information such as a copyright notice, a disclaimer, or a few links to relevant resources.')


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    header = models.ForeignKey(Header, on_delete=models.CASCADE, blank=True, null=True)
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, blank=True, null=True)
    result_html = models.FileField(blank=True, null=True)