from django import forms

class NewDepartamentoFrom(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellidos = forms.CharField(max_length=50, required=True)
    departamento = forms.CharField(max_length=50, required=True)
    shorname = forms.CharField(max_length=20, required=True)
    