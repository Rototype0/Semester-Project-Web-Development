from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name="game_lib_login"),
    path('logout_user', views.logout_user, name='game_lib_logout'),
    path('register_user', views.register_user, name='game_lib_register'),
]