from django import forms
from .models import Product

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','available_stock']

