from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
#from games_list.models import Game

# Create your models here.

class Review(models.Model):
    appid = models.IntegerField()
    header = models.CharField(max_length=100, default="Header")
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.header} (Game ID: {self.appid})"

class Rating(models.Model):
    appid = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    review = models.ForeignKey(
        Review,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="ratings"
    )

    def __str__(self):
        return f"Rating: {self.score} for Game ID: {self.appid}"

'''class Review(models.Model):
    appid = models.IntegerField()
    header = models.CharField(max_length=100, default="Header")
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.header} (Game ID: {self.appid})"

class Rating(models.Model):
    appid = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"Rating: {self.rating} for Game ID: {self.appid}"

class Review(models.Model):
    header = models.CharField(max_length=100, default="Header")
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes') #added likes to review class
    #rating = models.IntegerField(default = 0)
    #appid = models.ForeignKey(Game.appid, on_delete = models.CASCADE)
    #user = models.ForeignKey(Rating.user, on_delete = models.CASCADE)
    #def __str__(self):
    #   return f"{self.review.header}: {self.rating}"

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    review = models.ForeignKey(Review, on_delete = models.CASCADE)
    rating = models.IntegerField(default=0)
    #appid = models.ForeignKey(Game.appid, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.review.header}: {self.rating}"
    
class AppID(models.Model):
    review = models.ForeignKey(Review, on_delete = models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    appid = models.ForeignKey(Game.appid, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.appid}"
     '''

#def Upvotes(request, pk):
    #post = get_object_or_404
