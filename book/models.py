from __future__ import unicode_literals
from django.db.models import Model, CharField, TextField, DateTimeField, BigIntegerField, BooleanField
from django.db import models

# Create your models here.


class Book(Model):
    title = CharField(max_length=50)
    author = CharField(max_length=30)
    numOfView = BigIntegerField()
    content = TextField(max_length=10000)
