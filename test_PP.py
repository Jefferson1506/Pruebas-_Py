
from Appis import *

#Fase 1 : Escribir una prueba que falle : mensaje de hola
# def test_mensaje():
#   assert mesnajeHola();

#Fase 2 : Escribir una prueba que pase de obligatoria : mensaje de hola
# def test_mensaje():
#     return"Hello FastAPI"

#Fase 3 :Refactorización de la prueba : Mensaje de hola



def test_mensaje():
 a=mensajeHola(1)
 print(a)
 return a

def mensajeHola(X):
    if X == 1 :
      mensaje = "Hello FastAPI"
    
    if X !=1 and X>0: 
      mensaje = "HOLIS PAPU LINDO"
      return mensaje
    

#Fase 1 : Escribir una prueba que falle : Numero Primo
# def test_Primo():
#   assert verificar_primo()

#Fase 2 : Escribir una prueba que pase de obligatoria : Numero Primo
# def test_Primo():
#   return primoSI(3)

# def primoSI(X):
#   return True

#Fase 3 :Refactorización de la prueba : Numero Primo
def test_Primo():
  assert verificar_primo(3,100)


#Fase 1  : Escribir una prueba que falle : Serie fibonacci
# def test_Fibonacci():
#   assert fibonacci(4,100)

#Fase 2 : Escribir una prueba que pase de obligatoria : Serie fibonacci
# def test_Fibonacci():
#   return serieF(6)

# def serieF(X):
#  return X==8

#Fase 3 :Refactorización de la prueba : Serie fibonacci
def test_Fibonacci():
  assert fibonacci(6,100)





