import imp
from django import forms

class avionFormulario(forms.Form):
    marca = forms.CharField(max_length=60)
    capacidad = forms.IntegerField()
    anio_creacion = forms.IntegerField()