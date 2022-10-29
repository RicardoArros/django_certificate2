from inspect import ArgSpec

from django.shortcuts import render

from sqlite3 import IntegrityError
# from msilib.schema import Error

from .models import Certificado

#
def inicio(request):
  return render(request,"index.html")

#
def ingresar(request):
  return render(request,"ingresar.html")

#
def registro(request):
  #
  message = None
  
  #
  id_certificado = request.POST['id_certificado']
  nombre = request.POST['nombre']
  fecha = request.POST['fecha']
  curso = request.POST['curso']
  version = request.POST['version']
  id_verificacion = request.POST['id_verificacion']
  
  #
 
  Certificado.objects.create(id_certificado=id_certificado, nombre=nombre, fecha=fecha, curso=curso, version=version, id_verificacion=id_verificacion)
    
  message = 'se ha ingresado el certificado'
    
          
  return render(request,"registro.html", {'message': message})
  # except Error as err:
  #   message = f'ha ocurrido un problema en la operación_, {err}' 
      

#
def actualizar(request):
  return render(request,"actualizar.html")

#
def editar(request):
  #realizar actualizar
  pass

#
def listar(request):
  certificados = Certificado.objects.all()
  return render(request, "listar.html", {'certificados': certificados})

#
def validar(request):
  return render(request,"validar.html")

#
def valida(request):
  #realizar valida
  pass

#
def eliminar(request):
  return render(request,"eliminar.html")

#
def elimina(request):
  #realizar eliminar
  pass
