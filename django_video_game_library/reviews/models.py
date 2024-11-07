from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from games_list.models import Game
from django.db.models import Avg

# Create your models here.

class Review(models.Model):
    header = models.CharField(max_length=100, default="Header")
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    #author = models.ForeignKey(User, on_delete = models.CASCADE)
    #rating = models.IntegerField(default = 0)
    #appid = models.ForeignKey(Game.appid, on_delete = models.CASCADE)

    #def __str__(self):
    #    return f"{self.post.header}: {self.rating}"

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    review = models.ForeignKey(Review, on_delete = models.CASCADE)
    #appid = models.ForeignKey(Game.appid, on_delete = models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.post.header}: {self.rating}"

