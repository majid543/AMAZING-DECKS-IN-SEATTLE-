from django.db import models

# Create your models here.
class UserInput(models.Model):
    age = models.IntegerField()
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    deck_height = models.DecimalField(max_digits=5, decimal_places=2)