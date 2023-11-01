from django import forms

class CrearBandaFormulario(forms.Form):
    banda = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=250)
    precioEntrada = forms.IntegerField()