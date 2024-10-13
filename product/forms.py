from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category  # corrected from models to model
        fields = ['name', 'icon']
