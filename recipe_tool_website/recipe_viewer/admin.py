from django.contrib import admin

# Register your models here.

from .models import Material
from .models import Ingredient

admin.site.register(Material)
admin.site.register(Ingredient)
