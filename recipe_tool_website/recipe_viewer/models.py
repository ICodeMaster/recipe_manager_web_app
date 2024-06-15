from django.db import models
from django.urls import reverse

class Units(models.TextChoices):
    kgs  = 'kgs'
    lbs = 'lbs'
    g = 'g'
    oz = 'oz'
    floz = 'floz'
    tbsp = 'tbsp'
    tsp = 'tsp'
    gal = 'gal'
    #### Do some conversion math here in the enum

    def __str__(self) -> str:
        return str(self.name)
# Create your models here.
class Material(models.Model):
    name_str = models.CharField('Material Name', max_length=200)
    desc_str = models.CharField('Description', max_length=750, blank=True)
    cost = models.FloatField('Cost', default=0)
    cost_unit_amount = models.FloatField('Costing Amount', default=1.0)
    cost_unit = models.CharField(choices=Units.choices, default=Units.g, max_length=10)
    cost_per_unit = models.FloatField('Cost Per Unit', default=0.0)
    def __str__(self) -> str:
        return f"Material: {self.name_str}"
    def get_absolute_url(self):
        return reverse("recipe_viewer:material_view", kwargs={"pk": self.pk})
class ProceduralStep(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    step_desc = models.CharField('Description', max_length=1500, blank=True)
    step_material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)

class Recipe(models.Model):
    name_str = models.CharField('Material Name', max_length=200)
    desc_str = models.CharField('Description', max_length=750, blank=True)
    ingredients = models.ManyToManyField(Material, through="Ingredient")
    def __str__(self) -> str:
        return f"Recipe:{self.name_str}"
    @classmethod
    def get_default_pk(cls):
        recipe, created = cls.objects.get_or_create(
            defaults=dict(name_str='this is not an exam')
        )
        return recipe.pk
class Ingredient(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    unit = models.CharField(choices=Units.choices, default=Units.g, max_length=10)
    def __str__(self) -> str:
        return f"Ingredient:{self.material.name_str}"

