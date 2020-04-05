from django.db import models
from django.utils import timezone


class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    time = models.DateTimeField()
    picture = models.URLField(default="https://hh.ru/employer-logo/3184173.png")
    text = models.TextField()


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    author = models.CharField(max_length=500)
    text = models.TextField()


class UserInfo(models.Model):
    name = models.CharField(max_length=500)
    test = models.FloatField()


class Invite(models.Model):
    event = models.IntegerField()
    e_name = models.CharField(default="", max_length=500)
    name1 = models.CharField(max_length=500)
    name2 = models.CharField(max_length=500)
    submit = models.IntegerField()


class ChatID(models.Model):
    chat_id = models.IntegerField()
    name1 = models.CharField(max_length=500)
    name2 = models.CharField(max_length=500)


class Chat(models.Model):
    chat_id = models.IntegerField(default=0)
    name = models.CharField(max_length=500)
    text = models.TextField()
