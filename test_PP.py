
#Fase 1 : Escribir una prueba que falle : mensaje de hola
# def test_mensaje():
# assert mesnajeHola();

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







