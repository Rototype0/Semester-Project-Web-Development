from django.db import models

class Game(models.Model):
    appid = models.IntegerField()
    name = models.CharField(max_length=500)
    #review = models.ForeignKey(Review, on_delete=models.CASCADE)
    #rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    def __str__(self): 
         return str(self.appid)

class GameData(models.Model):
    appid = models.OneToOneField(Game, on_delete=models.CASCADE)
    is_free = models.BooleanField(default=False)
    detailed_description = models.TextField(default="no description was provided")
    supported_languages = models.TextField(default="english")
    short_description = models.TextField(default="no description was provided")
    header_image = models.URLField(default="no header image was provided")
    