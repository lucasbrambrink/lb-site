from django.contrib import admin
from .models import BlogPost


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'published',
        'created')


admin.site.register(BlogPost)