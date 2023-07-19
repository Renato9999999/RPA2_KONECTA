
import os
from datetime import datetime
from Txt import *

#variables
ruta_input = ""
ruta_output = ""
ruta_log = ""

#funciones
""" Descripcion, Funcion que se encarga de preparar el entorno para que el bot pueda 
    ejecutar correctamente, Obtiene el consolidado del contenido de las boletas de entrada

    Retorna una lista con los valores[estado, text_boletas, ruta_log]
"""
def configuracionInicial(ruta_config):
    
    #leer config para obtener las rutas de entrada del proceso
    rutas_entrada = leerConfig(ruta_config)
    
    #validar si la funcion leerConfig devolvio un error
    if not rutas_entrada:
        print("Error al leer config")
        return False
    
    ruta_input = rutas_entrada['ruta_input']
    ruta_output = rutas_entrada['ruta_output'] + "Boletas.pdf"
    ruta_log = rutas_entrada['ruta_log']
    correo_destino = rutas_entrada['correo_destino']
    correo_copia = rutas_entrada['correo_copia']
    
   
    
    #inicializar bandera de funcion
    estado = False
    text_boletas = ""
    
    #Fecha actual
    now = datetime.now()
    now = now.strftime("%m.%d.%Y_%H.%M.%S")
    
    #obtener ruta de registro con la fecha actual (donde se registraran los logs)
    ruta_log = ruta_log + "LOG_" + now + ".txt"

    #asignar diccionario de rutas del proceso obtenidas
    rutas = {'ruta_input': ruta_input, 'ruta_output': ruta_output, 'ruta_log': ruta_log, 'correo_destino': correo_destino, 'correo_copia': correo_copia}
    
    registrarLog("Inicia la configuracion del proceso", 1, ruta_log)
    #se lee el contenido del config
    with open(ruta_config) as f:
        contenido = f.read()

    #se obtienen todas las boletas de la carpeta input
    with os.scandir(ruta_input) as boletas:
        boletas = [boleta.name for boleta in boletas if boleta.is_file() and boleta.name.startswith('Boleta') and boleta.name.endswith('.txt')]
    
    registrarLog("Se encontraron " + str(len(boletas)) + " boletas", 1, ruta_log)
    if len(boletas) < 1:
        registrarLog("No se encontro ninguna boleta en la carpeta input", 0, ruta_log)
        return 2

    #se obtiene el contenido de cada boleta y se consolida todo en una variable
    for boleta in boletas:
        with open(ruta_input + boleta, encoding='utf-8') as f:
            contenido = f.read()
            text_boletas = text_boletas + contenido
    registrarLog("Se consolido todo el contenido de las boletas", 1, ruta_log)
   

    registrarLog("Finalizo funcion configuracion inicial", 1, ruta_log)
    estado = True
    return estado, text_boletas, rutas


