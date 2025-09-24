from django.db import models
from django import forms

class Developer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(default='test@example.com')
    age = models.IntegerField(default=0)


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    developers = models.ManyToManyField(Developer)

class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    developers = models.ForeignKey(Developer, on_delete=models.CASCADE)