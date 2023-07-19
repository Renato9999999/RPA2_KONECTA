from datetime import datetime

# functions

""" Descripcion: Funcion que se encarga de escribir en el registro local el mensaje
    ingresado por parametro.

    Retorna un valor boleano que indica si la funcion termino correctamnente o no
"""
def registrarLog(mensaje, tipo, ruta_log):
    
    estado = False
    
    #obtener Fecha actual
    now = datetime.now()
    now = now.strftime("%m.%d.%Y_%H.%M.%S")
    print(now)

    #establecer tipo de log
    if tipo == 0:
        tipo = "ERROR"
    else:
        tipo = "INFO"
    
    #personalizar mensaje de registro
    mensaje = "LOG_PROCESO_" + now + "|" + tipo + ": " + mensaje
    print(mensaje)
    
    #escribir el mensaje en una nueva linea del archivo de registro
    file1 = open(ruta_log, "a")
    file1.write("\n")
    file1.write(mensaje)
    file1.close()
    estado = True
    return estado
   
def leerConfig(ruta_config):
    variables = {}   # Diccionario que contendra los datos leidos.
    try:
        with open(ruta_config, "r") as datos:
            for linea in datos:
                nombre, valor = linea.strip().split("=", maxsplit=1)
                variables[nombre] = valor
    except Exception as e:
            print("Error al leer config: " + str(e))
            return False
    return variables

