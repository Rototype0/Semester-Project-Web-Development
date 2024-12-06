from django.contrib import admin
from games_list.models import *

# Register your models here.
#admin.site.register(Game)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('appid', 'name')
    search_fields = ('name',)

@admin.register(GameData)
class GameDataAdmin(admin.ModelAdmin):
    list_display = ('appid', 'short_description')
    search_fields = ('appid',)