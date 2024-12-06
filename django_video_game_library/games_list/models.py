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
    is_free = models.BooleanField()
    detailed_description = models.TextField()
    supported_languages = models.TextField(default="bruh")
    short_description = models.TextField()
    header_image = models.URLField()
    