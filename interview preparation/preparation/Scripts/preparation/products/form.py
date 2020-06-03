from django import forms

class ProductForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(decimal_places=2, max_digits=5)