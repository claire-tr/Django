from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db.models import Model, CharField, TextField


class Article(Model):
    title = CharField(max_length=50)
    content = TextField(max_length=3000)
