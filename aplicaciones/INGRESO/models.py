from django.db import models
from django.utils import timezone


class Turnos(models.Model):
    DOCTORES = (
        ("Sofia Diaz","Sofia Diaz"),
        ("Raul Vallejos","Raul Vallejos"),
    )
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    doctor=models.CharField(max_length=50,choices=DOCTORES)
    fecha=models.DateField(default=timezone.now)
    def __str__(self):
        return f"{self.apellido} {self.nombre} Doctor: {self.doctor}"

    class meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
        db_table = 'Turnos'
        ordering = ['apellido']




class Historial(models.Model):
    historia = models.TextField()
    fecha = models.DateField(default=timezone.now)
    def __str__(self):
        return f"{self.fecha}"
    class Meta:
        verbose_name = 'Historia'
        verbose_name_plural = 'Hitorial'
        db_table = 'Historial'
        ordering = ['fecha']



class Doctor1Pacientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    historial = models.ManyToManyField(Historial, blank=True, related_name="histor")
    def __str__(self):
        return f"{self.apellido} {self.nombre}"
    
    class Meta:
        verbose_name = 'PacientesDoctor1'
        verbose_name_plural = 'PacientesDoctor1'
        db_table = 'PacientesDoctor1'
        ordering = ['apellido']



class Doctor2Pacientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    historial = models.ManyToManyField(Historial,related_name="histo")
    def __str__(self):
        return f"{self.apellido} {self.nombre}"

    class Meta:
        verbose_name = 'PacientesDoctor2'
        verbose_name_plural = 'PacientesDoctor2'
        db_table = 'PacientesDoctor2'
        ordering = ['apellido']



