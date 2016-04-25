from __future__ import unicode_literals

from django.db.models import Model, CharField, TextField, DateTimeField, BigIntegerField, BooleanField
# Create your models here.


class BlogArticle(Model):
    title = CharField(max_length=50)
    authorID = BigIntegerField()
    timePost = DateTimeField()
    timeLastModify = DateTimeField()
    numOfView = BigIntegerField()
    allowComments = BooleanField()
    content = TextField(max_length=10000)


class BlogTag(Model):
    title = CharField(max_length=20)


class TagArticle(Model):
    blogId = BigIntegerField()
    tagId = BigIntegerField()

