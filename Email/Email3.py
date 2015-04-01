__author__ = 'Daniel'


#!/usr/bin/python
# -*- coding: utf-8 -*-
# Enviar correo Gmail con Python
# www.pythondiario.com

from email.mime.text import MIMEText
from smtplib import SMTP

def main():
 from_address = "micorreo@gmail.com"
 to_address = "correodestinatario@gmail.com"
 message = "Mensaje enviado desde python"
 mime_message = MIMEText(message)
 mime_message["From"] = from_address
 mime_message["To"] = to_address
 mime_message["Subject"] = "Correo de prueba"
 smtp = SMTP("smtp.gmail.com", 587)
 smtp.ehlo()
   smtp.starttls()
   smtp.ehlo()
 smtp.login(from_address, "clave")
 smtp.sendmail(from_address, to_address, mime_message.as_string())
 smtp.quit()
if __name__ == "__main__":
 main()
