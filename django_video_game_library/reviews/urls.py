from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', views.Home, name='reviews-home'),
    #path('about/', views.About, name='reviews-about'),
    #path('rate/<int:post_id>/<int:rating>/', views.rate),
    path('oreview/<int:review_id>/like/', views.like_review, name='like-review'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

