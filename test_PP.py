
from Appis import *
import pytest
import json
import requests

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


# EndPoint : 

ListaPrimoTest = [
  (1,False), 
  (2,True) , 
  (3,True) , 
  (4,False) , 
  (5,False)
  ]

ListaSeriefTest= [
(0, 0), 
(1, 1),
(2, 1),
(3, 2), 
(4, 3),
(5, 5),    
(6, 8)
]

@pytest.mark.parametrize("numero,expected",ListaPrimoTest)
def test_primoEnd(numero,expected):
    response = requests.post(f"http://127.0.0.1:8000/isPrime/{numero}")
    repuesta = json.loads(response.content)
    assert response.status_code ==200
    assert repuesta["validacion"]=="Solicitud Exitosa"
    assert repuesta["respuesta"]==expected


@pytest.mark.parametrize("numero,expected",ListaSeriefTest)
def test_primoEnd(numero,expected):
    response = requests.post(f"http://127.0.0.1:8000/fibonacci/{numero}")
    repuesta = json.loads(response.content)
    assert response.status_code ==200
    assert repuesta["validacion"]=="Solicitud Exitosa"
    assert repuesta["respuesta"]==expected 
