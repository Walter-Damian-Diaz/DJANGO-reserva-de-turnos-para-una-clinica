from django import forms
from .models import *

class FormularioTurnos(forms.ModelForm):
     class Meta:
        model = Turnos
        fields = '__all__'
        widgets = {
            'fecha' : forms.DateInput(attrs={ 'type': 'date' })
        }

class FormularioHistorial(forms.ModelForm):
    class Meta:
        model = Historial
        fields = '__all__'
        widgets = {'fecha' : forms.DateInput(attrs={'type':'date'})}

class FormularioDoctor1Pacientes(forms.ModelForm):
    class Meta:
        model = Doctor1Pacientes
        fields = ['nombre', 'apellido']

class FormularioDoctor2Pacientes(forms.ModelForm):
    class Meta:
        model = Doctor2Pacientes
        fields = ['nombre','apellido']
