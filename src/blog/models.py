from django.db import models
from django.contrib import admin
from markupfield.fields import MarkupField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    content = MarkupField(markup_type='markdown')

admin.site.register(Post)
