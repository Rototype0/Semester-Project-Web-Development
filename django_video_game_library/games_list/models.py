from django.db import models


class Game(models.Model):
    appid = models.IntegerField()
    name = models.CharField(max_length=500)
    def __str__(self): 
         return self.name