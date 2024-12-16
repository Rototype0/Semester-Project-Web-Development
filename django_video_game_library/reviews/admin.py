from django.contrib import admin
from .models import OReview, Rating
#from games_list.models import Game

# Register your models here.

@admin.register(OReview)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('header', 'appid', 'author', 'date_posted')
    list_filter = ('appid', 'author', 'date_posted')
    search_fields = ('header', 'content', 'author__username')
    ordering = ('-date_posted',)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('appid', 'user', 'score', 'review')
    list_filter = ('appid', 'user', 'score')
    search_fields = ('appid', 'user__username')
    ordering = ('appid', 'score')

#admin.site.register(Review)
#admin.site.register(Rating)