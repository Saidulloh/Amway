from django.contrib import admin

from apps.main.models import Main


@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
