from django.db import models
from django.utils import timezone


class Event(models.Model):
    id = models.IntegerField(help_text="ID", primary_key=True)
    name = models.CharField(max_length=500, help_text="Name")
    time = models.DateTimeField(help_text="Time")
    picture = models.URLField(default="https://hh.ru/employer-logo/3184173.png", help_text='Picture')
    text = models.TextField(help_text="Text")
