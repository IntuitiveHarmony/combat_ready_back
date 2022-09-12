from django.db import models

# Create your models here.
class Combatant(models.Model):
    name = models.CharField(max_length=40)
    intelligence = models.IntegerField()
    strength = models.IntegerField()
    speed = models.IntegerField()
    durability = models.IntegerField()
    power = models.IntegerField()
    combat = models.IntegerField()