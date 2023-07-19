import win32com.client
from Txt import *

#Funciones
""" Descripcion, Funcion que envia un email desde la cuenta de outlook activa.
    Se requiere tener instalado Outlook desktop y una sesion activa.

    Retorna un valor boleano que indica si la funcion termino correctamnente o no
"""
def enviarCorreo(adjunto, ruta_log, correo_destino, correo_copia):
    intentos = 0
    max_intentos = 3
    estado = False
    print("Inicia funcion para Enviar correo Outlook")
    
    while intentos < max_intentos:
        intentos +=1
        try:

            registrarLog("Inicia funcion EnviarCorreo, intento: " + str(intentos),1, ruta_log)
            
            ol=win32com.client.Dispatch("outlook.application")
            olmailitem=0x0
            newmail=ol.CreateItem(olmailitem)
            newmail.Subject= 'Reto Boletas'
            newmail.To=correo_destino
            newmail.CC=correo_copia
            newmail.Body= 'Estimados; Se adjunta el consolidado de boletas, \n\n Saludos; \n Renato Mendizabal.'
            newmail.Attachments.Add(adjunto)
            newmail.Display() # hacer visible correo
            newmail.Send()
            registrarLog("Se termino de enviar de correo",1, ruta_log)
            estado = True
            break
        
        except Exception as e:
            registrarLog("Error al enviar correo: " + str(e), 0, ruta_log)
            continue
    
    if estado:
        print("Finalizo correctamente funcion para Enviar correo Outlook")
    else:
        print("Error en funcion para Enviar correo Outlook")
    return estado
