from django import forms


class MaterialEditForm(forms.Form):
    material_name = forms.CharField(label="Material Name:", max_length=100)