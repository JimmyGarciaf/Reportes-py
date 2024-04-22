import smtplib #Este modulo proporciona funcionalidades para enviar correos electronicos utilizando el protocilo SMTP
from email.mime.multipart import MIMEMultipart # importa la clase MIMEMultipart del modulo email.mime.multipart basicamnete esta clase se utiliza para crear un mensaje de correo electrónico que puede contener partes múltiples, como texto y archivos adjuntos.
from email.mime.text import MIMEText # Similar al punto anterior se utiliza para crear partes de texto para el mensaje de correo electrónico.
import os #Esto importa el módulo os, que proporciona funciones para interactuar con el sistema operativo, como leer y escribir archivos, manipular rutas de archivo, y otras operaciones relacionadas con el sistema de archivos.

# Esta función se encarga de configurar y enviar un correo electrónico con los parámetros especificados.

def enviar_correo(destinatario, asunto, cuerpo, adjunto=None):
    # Configurar servidor SMTP
    servidor_smtp = 'smtp.gmail.com'
    puerto_smtp = 587
    usuario_smtp = 'jimmygarcia470@gmail.com'
    contraseña_smtp = 'jimmygaiden470'

    # Crear objeto mensaje
    #Este objeto permite adjuntar múltiples partes al mensaje, como texto plano, archivos adjuntos, imágenes, etc.
    mensaje = MIMEMultipart()
    # El remitente dle msj
    mensaje['From'] = usuario_smtp
    #Esto me indicara a quién se enviará el correo electrónico.
    mensaje['To'] = destinatario
    #Establezco el asunto del correo.
    mensaje['Subject'] = asunto

    # Adjuntar cuerpo del correo
    # Se utiliza MIMEText para crear una parte de texto plano del mensaje, y el metodo attach se utiliza para adjuntar al msj principal
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Adjuntar archivo si existe
    if adjunto: #Se verifica si se ha proporcionado un archivo adjunto.
        adjunto_mime = MIMEText(open(adjunto, 'rb').read(), 'plain') #Se abre el archivo adjunto pero en modo lectura binaria('rb') y se lee el contenido y creamos una instancia del mismo
        adjunto_mime.add_header('Content-Disposition', f'attachment; filename={os.path.basename(adjunto)}') #Se utiliza os.path.basename(adjunto) para obtener solo el nombre del archivo sin la ruta completa.
        mensaje.attach(adjunto_mime) #Se adjunta la parte del archivo al mensaje principal utilizando el método attach()
        
     # Iniciar conexión SMTP y enviar correo
     # Se inicia una conexión SMTP con el servidor SMTP 
     # Basicamnete hacemos una conexion segura al servidor SMTP.
     # El contexto 'with' nos garantiza que la conexión se cierre adecuadamente al finalizar la operación.
    with smtplib.SMTP(servidor_smtp, puerto_smtp) as servidor:
        servidor.starttls() #Se inicia la capa de seguridad TLS, mas que todo para cifrar la comunicación entre el cliente y el servidor
        servidor.login(usuario_smtp, contraseña_smtp)#Aqui vamos autentificar en el servidor SMTP utilizando el nombre de usuario y la contraseña.
        servidor.send_message(mensaje)# Enviamos el msj de correo.

    print("Correo enviado con éxito!")#Y por ultimo verificamos con un msj de consola que se envio el correo.