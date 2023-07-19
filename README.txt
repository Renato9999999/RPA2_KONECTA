RPA para automatizar generacion de pdf consolidado de boletas
El robot lee un boletas en txt, que deben estar en la carpeta Input
Genera un PDF de todos los txt unidos y lo guarda en la carpeta Output
Finalmente envia un correo con el pdf por outlook desktop.
(Los destinatarios se pueden configurar en el ./Robot/Config.txt al igual que las rutas)
El robot registra un log de auditoria del proceso que se almacena en la carpeta Logs

Prerequisitos
Se necesita tener instalado:
	Python 3.9
	Outlook instalado, con una cuenta en sesion iniciada.
	Se necesita que el proyecto se clone desde el repositorio remoto y se respete la estructura de 
	carpetas definida (C:\RPA2_KONECTA esta debe ser la carpeta principal), en caso que se cambie la ruta, las rutas del robot se deben configurar en el Config.txt

Instalacion:

Clone el proyecto, y ejecute el Main.bat que esta en la carpeta principal, para ejecutar la automatizacion.
isntalar las librerias indicadas en requeriments.txt, puede utilizar el comando: pip install -r requirements.txt


