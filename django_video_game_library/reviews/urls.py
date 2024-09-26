from django.urls import path
from . import views

urlpatterns = [
    path('', views.Demo, name='reviews-demo'),
    path('home', views.Home, name='reviews-home'),
    path('about/', views.About, name='reviews-about'),
]
