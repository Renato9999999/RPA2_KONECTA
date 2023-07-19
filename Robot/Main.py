from Configuracion import *
from Correo import *
from PDF import *
from Txt import *


#variables del proceso
ruta_config = './Config.txt'
intentos = 0
max_intentos = 3
estado_proceso = False

#preparar el entorno del bot y obtiene los datos de entrada del proceso
resultado_config = configuracionInicial(ruta_config)
if resultado_config == 2:
    print("No se encontro ninguna boleta en la carpeta input")
    exit()

#asignar valriables obtenidas
text_boletas = resultado_config[1]
rutas = resultado_config[2]
ruta_log = rutas['ruta_log']
ruta_output = rutas['ruta_output']
correo_destino = rutas['correo_destino']
correo_copia = rutas['correo_copia']

#validar que el bot este preparado para los siguientes pasos
if not resultado_config[0]:
     print("Error en configuracion inicial del bot")
     exit()

print("Inicia proceso: Consolidar Boletas")
#flujo principal del proceso, se establecen reintentos en caso de error de alguna funcion
while intentos < max_intentos:
    intentos +=1
    print("Inicia intento " + str(intentos))
   
    if not exportarPDF(text_boletas, ruta_output, ruta_log):
        print("Error al exportar pdf")
        continue
    
    if not enviarCorreo(ruta_output, ruta_log, correo_destino, correo_copia):
        print("Error al enviar correo con las boletas del proceso")
        continue
    #Se levanta la bandera, lo que indica que el proceso finalizo correctamente
    estado_proceso = True
    break

if estado_proceso:
    print("El proceso finalizo correctamente")
else:
    print("El proceso finalizo con error")
   