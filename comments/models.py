import django
from django.db import models


# Create your models here.


class Comment(models.Model):
    title = models.CharField(default='default title', max_length=255)
    body = models.TextField(default='default body text')
    author = models.CharField(default='Name', max_length=127)
    date = models.DateField(default=django.utils.timezone.now)
