import aspose.pdf as ap
import os.path
from Txt import *


""" Descripcion: Funcion que se encarga de crear un pdf con el texto ingresado
    como parametro

    Retorna un valor boleano que indica si la funcion termino correctamnente o no
"""
def exportarPDF(texto, ruta_output, ruta_log):
    
    #se asignan las variables del proceso
    estado = False
    intentos = 0
    max_intentos = 3

    #flujo de la funcion, se establecen reintentos en caso de error
    while intentos < max_intentos:
        try:
            intentos +=1
            #validar si output ya existe en ruta local
            check_file = os.path.isfile(ruta_output)
            print("Output existe: " + str(check_file))
        
            if check_file:
                registrarLog("Se intentara eliminar pdf existente: " + ruta_output, 1, ruta_log)
                os.remove(ruta_output)
                registrarLog("Se elimino pdf",1, ruta_log)
            
            # inicializar objeto tipo documento
            documento = ap.Document()

            # se añade pagina
            pagina = documento.pages.add()

            # se inicializa un area de texto
            area_texto = ap.text.TextFragment(texto)

            # Se añade area de texto
            pagina.paragraphs.add(area_texto)

            # se exporta y guarda el pdf en la ruta ingresada por parametro
            documento.save(ruta_output)
            estado = True
        except Exception as e:
            registrarLog("Error al enviar correo: " + str(e), 0, ruta_log)
            continue
    
    registrarLog("Termino de generar pdf: ", 1, ruta_log)
    return estado
