from django.contrib import admin
from demo_api       import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [ 'title' ]


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [ 'body' ]
