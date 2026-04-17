from django.contrib import admin
from apps.blog.models import BlogPost , BlogTag

# Register your models here.

admin.site.register(BlogPost),
admin.site.register(BlogTag)