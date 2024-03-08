from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpRequest, HttpResponseRedirect
from django.template import loader

from .models import Material, Ingredient
from .forms import MaterialEditForm

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
def material_edit_view(request: HttpRequest, material_id):
    if request.method == "POST":
        form = MaterialEditForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("")
    else:
        form = MaterialEditForm()
    context = {"form": form}
    return render(request, "recipe_viewer/material_edit.html", context)