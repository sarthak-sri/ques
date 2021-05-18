from django.contrib import admin
from .models import Blogpost
from . import models
from mptt.admin import MPTTModelAdmin
# Register your models here.
admin.site.register(Blogpost)

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }



admin.site.register(models.Category)

admin.site.register(models.Comment,MPTTModelAdmin)
