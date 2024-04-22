import smtplib #Este modulo proporciona funcionalidades para enviar correos electronicos utilizando el protocilo SMTP
from email.mime.multipart import MIMEMultipart # importa la clase MIMEMultipart del modulo email.mime.multipart basicamnete esta clase se utiliza para crear un mensaje de correo electrónico que puede contener partes múltiples, como texto y archivos adjuntos.
from email.mime.text import MIMEText # Similar al punto anterior se utiliza para crear partes de texto para el mensaje de correo electrónico.
import os #Esto importa el módulo os, que proporciona funciones para interactuar con el sistema operativo, como leer y escribir archivos, manipular rutas de archivo, y otras operaciones relacionadas con el sistema de archivos.

