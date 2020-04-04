from django.db import models
from django.utils import timezone


class Event(models.Model):
    id = models.IntegerField(help_text="ID", primary_key=True)
    name = models.CharField(max_length=500)
    time = models.DateTimeField()
    picture = models.URLField(default="https://hh.ru/employer-logo/3184173.png")
    text = models.TextField()


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    author = models.CharField(max_length=500)
    text = models.TextField()