from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class OReview(models.Model):
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
        OReview,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="ratings"
    )

    def __str__(self):
        return f"Rating: {self.score} for Game ID: {self.appid}"
