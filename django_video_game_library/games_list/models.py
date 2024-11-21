from django.db import models
from reviews.models import Review, Rating


class Game(models.Model):
    appid = models.IntegerField()
    name = models.CharField(max_length=500)
    #review = models.ForeignKey(Review, on_delete=models.CASCADE)
    #rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    def __str__(self): 
         return self.name