from django import forms


class RecipeEditForm(forms.Form):
    name_str = forms.CharField(label='Material Name: ', max_length=200)
    desc_str = forms.CharField(label='Description: ', max_length=750, blank=True)