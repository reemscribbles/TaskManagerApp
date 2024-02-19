from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(default=date.today)
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete', 'due_date', ]

class Habit(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    streak = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['streak', 'title', ]


class Parent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    t = Task
    h=Habit
