from django.db import models

# Create your models here.

class Weapon(models.Model):
    name = models.CharField(max_length=100)
    damage = models.IntegerField()
    version = models.CharField(max_length=50)

class Object(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class PowerUp(models.Model):
    name = models.CharField(max_length=100)
    effect = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    