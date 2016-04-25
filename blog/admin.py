from django.contrib import admin
from blog.models import BlogArticle, BlogTag, TagArticle

# Register your models here.
admin.site.register(BlogArticle)
admin.site.register(BlogTag)
admin.site.register(TagArticle)
