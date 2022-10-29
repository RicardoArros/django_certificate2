from django.db import models

from datetime import date

# Create your models here.

class Certificado(models.Model):  
  id_certificado = models.CharField(max_length=30, primary_key=True)
  nombre = models.CharField(max_length=50, null=False)
  fecha = models.DateField(null=False, verbose_name="Fecha (dd/mm/yyyy)")
  curso = models.CharField(max_length=30, null=False)
  version = models.CharField(max_length=15, null=False)
  id_verificacion = models.CharField(max_length=15, unique=True, null=False)
    
  def __str__(self):
    return self.nombre

  # def __unicode__(self):
  #   return 
