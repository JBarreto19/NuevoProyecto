from django import forms

class CrearBandaFormulario(forms.Form):
    banda = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=250)
    precioEntrada = forms.IntegerField()
    
class CrearVenueFormulario(forms.Form):
    Nombre = forms.CharField(max_length=30)
    Direccion = forms.CharField(max_length=250)
    capacidad = forms.IntegerField()