from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpRequest, HttpResponseRedirect
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView

from .models import Material, Ingredient

# Create your views here.
def index(request):
    material_list = Material.objects.order_by("-id")[:50]

    context = {
        "material_list": material_list,
    }
    return render(request, "recipe_viewer/index.html", context)
class MaterialDetailView(DetailView):
    model = Material
    template_name = "recipe_viewer/material_view.html"

class MaterialCreateView(CreateView):
    model = Material
    fields = ["name_str", "desc_str", "cost", "cost_unit", "cost_unit_amount"]
    success_url = reverse_lazy("recipe_viewer:index")
    def form_valid(self, form):
        cost = form.instance.cost
        cost_unit_amount = form.instance.cost_unit_amount
        cost_per_unit = cost/cost_unit_amount
        form.instance.cost_per_unit = cost_per_unit
        return super().form_valid(form)
class MaterialEditView(UpdateView):
    model = Material
    fields = ["name_str", "desc_str", "cost", "cost_unit", "cost_unit_amount"]
class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy("recipe_viewer:index")