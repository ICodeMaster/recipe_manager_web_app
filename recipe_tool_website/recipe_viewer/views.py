from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Material, Ingredient

# Create your views here.
def index(request):
    material_list = Material.objects.order_by("-id")[:50]

    context = {
        "material_list": material_list,
    }
    return render(request, "recipe_viewer/index.html", context)
def material_view(request, material_id):
    try:
        material = Material.objects.get(pk=material_id)
        context = {
            "material": material
        }
    except Material.DoesNotExist:
        raise Http404("Material does not exist")
    return render(request, "recipe_viewer/material_view.html", context)