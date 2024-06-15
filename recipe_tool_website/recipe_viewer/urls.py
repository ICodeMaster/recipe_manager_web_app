from django.urls import path
from . import views

app_name = "recipe_viewer"
urlpatterns = [
     path("", views.index, name="index"),
     path("material/<int:pk>/view/", views.MaterialDetailView.as_view(), name="material_view"),
     path("material/create", views.MaterialCreateView.as_view(), name="material-create-view"),
     path("material/<int:pk>/edit", views.MaterialEditView.as_view(), name="material-edit-view"),
     path("material/<int:pk>/delete/", views.MaterialDeleteView.as_view(), name="material-delete-view"),
     #### Recipes
     path("recipe/<int:pk>/edit", views.RecipeEditView.as_view(), name="recipe-edit-view"),
     path("recipe/create", views.RecipeCreateView.as_view(), name="recipe-create-view"),
]