from django.urls import path
from .views.logs.views import *
from .views.secretarias.views import *
from .views.doctores.views import *

app_name='INGRESO'
urlpatterns = [
    #Inicio de sesion
    path("login", Logs.login_view, name="login"),
    path("inicio", Logs.inicio ,name="inicio"),
    path("salir", Logs.salir, name="salir"),
    #Secretaria
    path("asignar",AsignarPaciente.enviar_formulario,name="asignar"),
    path("procesar",AsignarPaciente.procesar_formulario,name="procesar"),
    path("lista_turnos",ListaTurnos.lista_turnos,name="lista_turnos"),
    path("editar/<id>",ListaTurnos.editar,name="editar"),
    path("eliminar/<id>",ListaTurnos.eliminar,name="eliminar"),
    #Doctores
    path("listaPacientesDoc1",Doctor1.lista,name="listaPacientesDoc1"),
    path("historialDoc1/<id>",Doctor1.historia,name="historialDoc1"),
    path("agregar_historiaDoc1/<id>",Doctor1.agregar,name="agregar_historiaDoc1"),
    path("listaPacientesDoc2",Doctor2.lista,name="listaPacientesDoc2"),
    path("historialDoc2/<id>",Doctor2.historia,name="historialDoc2"),
    path("agregar_historiaDoc2/<id>",Doctor2.agregar,name="agregar_historiaDoc2"),
]
