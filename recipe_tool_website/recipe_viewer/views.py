from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpRequest, HttpResponseRedirect
from django.template import loader

from django.views.generic.edit import CreateView

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

class MaterialCreateView(CreateView):
    model = Material
    fields = ["name_str", "desc_str", "cost", "cost_unit"]

    def form_valid(self, form):
        form.instance.cost_per_unit =
        return super().form_valid(form)