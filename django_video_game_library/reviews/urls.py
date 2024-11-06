from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='reviews-home'),
    #path('home/', views.Home, name='reviews-home'),
    path('about/', views.About, name='reviews-about'),
]
