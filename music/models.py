# music/models.py
from django.db import models

class Mood(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} by {self.artist}'
