from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from aplicaciones.INGRESO.models import *
from aplicaciones.INGRESO.forms import *

class Doctor2(HttpRequest):
    def lista(request):
        pacientes = Doctor2Pacientes.objects.all()
        return render(request,"doctores/pacientesDoc2.html",{
            "pacientes": pacientes
        })

    def historia(request,id):
        paciente = Doctor2Pacientes.objects.get(id=id)
        historia = paciente.historial.all()
        return render (request,"doctores/historialDoc2.html",{
            "historial" : historia,
            "paciente" : paciente
        })
    def agregar(request,id):
        form = FormularioHistorial()
        paciente = Doctor2Pacientes.objects.get(id=id)
        if request.method == 'POST':
            historia = FormularioHistorial(request.POST)
            if historia.is_valid():
                historia = historia.save()
                paciente.historial.add(historia)
                return redirect(to='INGRESO:listaPacientesDoc2')
        return render(request,"doctores/agregarHistorialDoc2.html",{
            'form':form,
            'paciente':paciente,
        })

class Doctor1(HttpRequest):
    def lista(request):
        pacientes = Doctor1Pacientes.objects.all()
        return render(request,"doctores/pacientesDoc1.html",{
            "pacientes": pacientes
        })
        
    def historia(request,id):
        paciente = Doctor1Pacientes.objects.get(id=id)
        historia = paciente.historial.all()
        return render (request,"doctores/historialDoc1.html",{
            "historial" : historia,
            "paciente" : paciente
        })
    def agregar(request,id):
        form = FormularioHistorial()
        paciente = Doctor1Pacientes.objects.get(id=id)
        if request.method == 'POST':
            historia = FormularioHistorial(request.POST)
            if historia.is_valid():
                historia = historia.save()
                paciente.historial.add(historia)
                return redirect(to='INGRESO:listaPacientesDoc1')
        return render(request,"doctores/agregarHistorialDoc1.html",{
            'form':form,
            'paciente':paciente,
        })
        



