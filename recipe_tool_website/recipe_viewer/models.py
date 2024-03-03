from django.db import models
from enum import Enum

class Units(Enum):
    kgs  = 1
    lbs = 2
    g = 3
    oz = 4
    floz = 5
    tbsp = 6
    tsp = 7
    gal = 8
    #### Do some conversion math here in the enum

    def __str__(self) -> str:
        return str(self.name)
# Create your models here.
class Material(models.Model):
    name_str = models.CharField(max_length=200)
    desc_str = models.CharField(max_length=750)
    cost = models.IntegerField(default=0)
class Ingredient(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    unit = models.CharField(max_length=30)
