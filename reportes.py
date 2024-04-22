import smtplib #Este modulo proporciona funcionalidades para enviar correos electronicos utilizando el protocilo SMTP
from email.mime.multipart import MIMEMultipart # importa la clase MIMEMultipart del modulo email.mime.multipart basicamnete esta clase se utiliza para crear un mensaje de correo electrónico que puede contener partes múltiples, como texto y archivos adjuntos.
from email.mime.text import MIMEText # Similar al punto anterior se utiliza para crear partes de texto para el mensaje de correo electrónico.
import os #Esto importa el módulo os, que proporciona funciones para interactuar con el sistema operativo, como leer y escribir archivos, manipular rutas de archivo, y otras operaciones relacionadas con el sistema de archivos.

# Esta función se encarga de configurar y enviar un correo electrónico con los parámetros especificados.

def enviar_correo(destinatario, asunto, cuerpo, adjunto=None):
    # Configurar servidor SMTP
    servidor_smtp = 'corporacion@mcc.hn'
    puerto_smtp = 587
    usuario_smtp = 'jgarcia@mcc.hn'
    contraseña_smtp = 'Garcia.2024'

    # Crear objeto mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = usuario_smtp
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto

    # Adjuntar cuerpo del correo
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Adjuntar archivo si existe
    if adjunto:
        adjunto_mime = MIMEText(open(adjunto, 'rb').read(), 'plain')
        adjunto_mime.add_header('Content-Disposition', f'attachment; filename={os.path.basename(adjunto)}')
        mensaje.attach(adjunto_mime)
        
     # Iniciar conexión SMTP y enviar correo
    with smtplib.SMTP(servidor_smtp, puerto_smtp) as servidor:
        servidor.starttls()
        servidor.login(usuario_smtp, contraseña_smtp)
        servidor.send_message(mensaje)

    print("Correo enviado con éxito!")