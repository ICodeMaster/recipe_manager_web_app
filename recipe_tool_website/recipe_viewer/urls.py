from django.urls import path
from . import views

app_name = "recipe_viewer"
urlpatterns = [
     path("", views.index, name="index"),
     path("material/<int:material_id>/view/", views.material_view, name="material_view"),
     path("material/create", views.MaterialCreateView.as_view(), name="material_create_view"),
]