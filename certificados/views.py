from inspect import ArgSpec
from django.shortcuts import render
from sqlite3 import IntegrityError
#from msilib.schema import Error

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
  try:
    Certificado.objects.create(id_certificado=id_certificado, nombre=nombre, fecha=fecha, curso=curso, version=version, id_verificacion=id_verificacion)    
    message = 'se ha ingresado el certificado' 

  except Exception as ex:
    if str(ex.__cause__).find('prueba2_certificado.id_certificado') > 0:
      message = 'ha ocurrido un problema en la operación, id ya ingresado'
      
    elif str(ex.__cause__).find('prueba2_certificado.id_verificacion') > 0:
      message = 'ha ocurrido un problema en la operación, id ya ingresado'
      
    else:
      message = 'ha ocurrido un problema en la operación'
  
  except Error as err:
    message = f'ha ocurrido un problema en la operación_, {err}'

  #
  return render(request,"registro.html", {'message': message})


#
def actualizar(request):
  return render(request,"actualizar.html", {"form2": "hidden"})


#
def editar(request):
  #
  cert = None  
  message = ""  
  visibilidad = ""
  
  #
  try:
    cert = Certificado.objects.get(id_certificado = request.GET["txtValidador"])
    
    visibilidad = "visible"
    
    return render(request, "actualizar.html", {"form2": visibilidad, "c": cert})  
  except:
    cert = None
  
  #
  if cert == None:
    id_certificado = None
    
    try:
      id_certificado = request.POST["id_certificado"]
    except:
      id_certificado = None

    if id_certificado != None:
      cert = Certificado.objects.get(id_certificado = id_certificado)        
    
      nombre = request.POST['nombre']
      fecha = request.POST['fecha']
      curso = request.POST['curso']
      version = request.POST['version']
      idVerificacion = request.POST['id_verificacion']       

      cert.nombre = nombre
      cert.fecha = fecha
      cert.curso = curso
      cert.version = version
      cert.id_verificacion = idVerificacion

      try:
        cert.save()
        message = "Se ha actualizado el certificado"
      except:
        message = "Se ha ocurrido un error al actualizar el certificado"

      visibilidad = "hidden"
      
      return render(request, "actualizar.html", {"message": message, "form2": visibilidad})
    
    else:
      message = "No se ha encontrado el certificado"
      visibilidad = "hidden"
      
      return render(request, "actualizar.html", {"message": message, "form2": visibilidad})
  else:
      message = "No se encontró el certificado solicitado"
      visibilidad = "hidden"
      return render(request, "actualizar.html", {"message": message, "form2": visibilidad})
  

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

