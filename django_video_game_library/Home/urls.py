from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


'''urlpatterns = [
    #path('', views.Home, name='reviews-home'),
    path('about/', views.About, name='reviews-about'),
    #path('rate/<int:post_id>/<int:rating>/', views.rate),
    path('', views.Home, name='reviews-home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
'''

urlpatterns = [
    path('', include("games_list.urls"), name='home'),
    path('auth/', include("user_authentication.urls",)),
    path('about/', views.About, name='about'),
]