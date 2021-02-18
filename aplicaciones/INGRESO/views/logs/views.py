from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class Logs(HttpRequest):
    
    def login_view(request):
        if request.method == 'POST':
            usuario = request.POST["usuario"]
            contraseña = request.POST["contraseña"]
            user = authenticate(request,username=usuario,password=contraseña)
            if user:
                login(request,user)
                return redirect(to='INGRESO:inicio')
            else:
                return render(request,"logs/login.html",{
                    "mensajeError":"error",
                })
        return render(request,"logs/login.html")
    
    def inicio(request):
        if not request.user.is_authenticated:
            return redirect(to='INGRESO:login')
        return render(request,"logs/inicio.html")

    def salir(request):
        logout(request)
        return redirect(to='INGRESO:login')


        