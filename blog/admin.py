from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from . import models

# Register your models here.


@admin.register(models.PostFilesModel)
class PostFilesAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'download_count')
    search_fields = ['title', ]
    exclude = ['download_count', ]


@admin.register(models.BotUserModel)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'first_name', 'last_name', 'username', 'created', 'updated')
    search_fields = ['chat_id', 'first_name', 'username', ]


@admin.register(models.CategoryModel)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'parent',)
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', ]
