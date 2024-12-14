from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name="game_lib_login"),
    path('logout_user', views.logout_user, name='game_lib_logout'),
    path('register_user', views.register_user, name='game_lib_register'),
    path('update_user', views.update_user, name='game_lib_update_user'),
    path('update_password', views.update_password, name='game_lib_update_password'),
]