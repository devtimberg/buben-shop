from django import forms


class FilterForm(forms.Form):
    min_price = forms.DecimalField(max_digits=8, decimal_places=2)
    max_price = forms.DecimalField(max_digits=8, decimal_places=2)