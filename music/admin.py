# music/admin.py
from django.contrib import admin
from .models import Mood, Song

admin.site.register(Mood)
admin.site.register(Song)
