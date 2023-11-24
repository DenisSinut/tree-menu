from django.contrib import admin
from tree_menu.models import Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'url', 'named_url']
    fields = ['name', 'parent', 'url', 'named_url']
    search_fields = ['name', 'parent']
    ordering = ['name']

# Register your models here.
