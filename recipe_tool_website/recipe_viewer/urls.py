from django.urls import path
from . import views

app_name = "recipe_viewer"
urlpatterns = [
     path("", views.index, name="index"),
     path("material/<int:pk>/view/", views.MaterialDetailView.as_view(), name="material_view"),
     path("material/create", views.MaterialCreateView.as_view(), name="material_create_view"),
     path("material/<int:pk>/edit", views.MaterialEditView.as_view(), name="material_edit_view"),
     path("material/<int:pk>/delete/", views.MaterialDeleteView.as_view(), name="material-delete-view"),
]