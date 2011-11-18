from django.db import models
from django.contrib import admin
from markupfield.fields import MarkupField

class Post(models.Model):
    title = models.CharField(max_length=300)
    content = MarkupField(markup_type='markdown')
    pub_date = models.DateField(auto_now_add=True)
    last_modification_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
