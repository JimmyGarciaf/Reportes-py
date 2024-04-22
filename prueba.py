import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_correo(destinatario, asunto, cuerpo):
    # Configurar servidor SMTP de Gmail
    servidor_smtp = 'smtp.gmail.com'
    puerto_smtp = 587  # Puerto TLS de Gmail

    # Tu dirección de correo electrónico de Gmail y contraseña
    usuario_smtp = 'jimmygarcia470@gmail.com'
    contraseña_smtp = 'Jimmygarcia470'

    # Crear objeto mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = usuario_smtp
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto

    # Adjuntar cuerpo del correo
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Iniciar conexión SMTP y enviar correo
    with smtplib.SMTP(servidor_smtp, puerto_smtp) as servidor:
        servidor.starttls()  # Iniciar conexión TLS
        servidor.login(usuario_smtp, contraseña_smtp)  # Autenticación con Gmail
        servidor.send_message(mensaje)  # Envío del mensaje

    print("Correo enviado con éxito!")

# Ejemplo de uso
destinatario = 'santosgarcia2355@gmail.com'
asunto = 'Prueba de correo desde Python'
cuerpo = 'Este es un correo de prueba enviado desde Python utilizando el servidor SMTP de Gmail.'

enviar_correo(destinatario, asunto, cuerpo)