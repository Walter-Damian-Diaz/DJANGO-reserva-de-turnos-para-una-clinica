from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from aplicaciones.INGRESO.forms import *
from aplicaciones.INGRESO.models import *

class AsignarPaciente(HttpRequest):
    
    def enviar_formulario(request):
        data = {
            'form': FormularioTurnos()
        }
        return render(request,"secretarias/asignarPaciente.html",data)
    
    def procesar_formulario(request):
        if request.method == 'POST':
            turno = FormularioTurnos(request.POST)
            if turno.is_valid():
                turn=turno.save()
                if turn.doctor == "Sofia Diaz":
                    pacientes1=Doctor1Pacientes(nombre=turn.nombre,apellido=turn.apellido)
                    pacientes1.save()
                else:
                    pacientes2=Doctor2Pacientes(nombre=turn.nombre,apellido=turn.apellido)
                    pacientes2.save()
                return redirect(to='INGRESO:inicio')
            else:
                data = {
                    'form':FormularioTurnos()
                }
                return render(request,"secretarias/asignarPaciente.html",data)
        return render(request,"secretarias/asignarPaciente.html",{
                    'form': FormularioTurnos()
                })


class ListaTurnos(HttpRequest):
    
    def lista_turnos(request):
        data={
            "turnos":Turnos.objects.all()
        }
        return render(request,"secretarias/lista-turnos.html",data)
    
    def editar(request,id):
        turno = Turnos.objects.get(id=id)
        form = FormularioTurnos(instance=turno)
        if request.method == 'POST':
            turno = FormularioTurnos(data=request.POST,instance=turno)
            if turno.is_valid():
                turno.save()
                return redirect(to='INGRESO:lista_turnos')
        return render(request,"secretarias/editar.html",{
            'form':form
        })
    def eliminar(request,id):
        turno = Turnos.objects.get(id=id)
        turno.delete()
        return redirect(to='INGRESO:lista_turnos')
        



