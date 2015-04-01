__author__ = 'Daniel'

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Enviar correo Gmail con Python
# www.pythondiario.com

import smtplib, socket, sys, getpass

def main():

 # Conexion con el servidor
 try:
  smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.ehlo()
  print "Conexion exitosa con Gmail"
  print "Concectado a Gmail"
  # Datos
  try:
   gmail_user = str(raw_input("Escriba su correo: ")).lower().strip()
   gmail_pwd = getpass.getpass("Escriba su password: ").strip()
   smtpserver.login(gmail_user, gmail_pwd)
  except smtplib.SMTPException:
   print ""
   print "Autenticacion incorrecta" + "\n"
   smtpserver.close()
   getpass.getpass("Presione ENTER para continuar...")
   sys.exit(1)


 except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
  print "Fallo en la conexion con Gmail"
  print getpass.getpass("Presione ENTER para continuar...")
  sys.exit(1)


 while True:
  to = str(raw_input("Enviar correo a: ")).lower().strip()
  if to != "":
   break
  else:
   print "El correo es necesario!!!"

 sub = str(raw_input("Asunto: ")).strip()
 bodymsg = str(raw_input("Mensaje: "))
 print ""
 header = "Para: " + to +"\n" + "De: " + gmail_user + "\n" + "Asunto: " + sub + "\n"
 print header
 msg = header + "\n" + bodymsg + "\n\n"
 print msg

 try:
  smtpserver.sendmail(gmail_user, to, msg)
 except smtplib.SMTPException:
  print "El correo no pudo ser enviado" + "\n"
  smtpserver.close()
  getpass.getpass("Presione ENTER para continuar...")
  sys.exit(1)

 print "El correo se envio correctamente" + "\n"
 smtpserver.close()
 getpass.getpass("Presione ENTER para continuar")
 sys.exit(1)


main()