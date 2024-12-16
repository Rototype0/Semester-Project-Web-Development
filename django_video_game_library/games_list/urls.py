from django.contrib import admin
from django.urls import path, include
from . import views
from reviews.views import OReviews

urlpatterns = [
    path('importjson/', views.import_data, name='import_json'),
    path('', views.Games_List, name='games_list'),
    path('game/<str:appid>/', views.Game_Info, name='game_lib_game'),
    path('game/<int:appid>/reviews/', OReviews, name='game_lib_oreviews'),

]
