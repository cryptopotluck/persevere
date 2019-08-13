from django.contrib import admin

from .models import Question, Reply
# Register your models here.


class PetsPost(admin.ModelAdmin):
    list_display = ['language', 'post_title']
    list_display_links = ['language', 'post_title']
    list_per_page = 25


admin.site.register(Question, PetsPost)


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'pub_date']
    list_display_links = ['post', 'author', 'pub_date']
    list_per_page = 25


admin.site.register(Reply, ReplyAdmin)