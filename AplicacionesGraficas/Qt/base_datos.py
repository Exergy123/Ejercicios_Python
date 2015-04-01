__author__ = 'Daniel'

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Aplicacion grafica con sqlite3
# www.pythondiario.com

import sys
import sqlite3
from PyQt4 import QtCore, QtGui, uic

# Cargar nuestro archivo .ui
form_class = uic.loadUiType("conBase.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
 def __init__(self, parent=None):
  QtGui.QMainWindow.__init__(self, parent)
  self.setupUi(self)
  self.btn_Guardar.clicked.connect(self.btn_Guardar_clicked)
  self.btn_Cargar.clicked.connect(self.btn_Cargar_clicked)
  self.IniciarBase()


 def IniciarBase(self):
  self.con = sqlite3.connect("/home/diego123/Escritorio/pyqt4/prueba.bd")
  self.cursor = self.con.cursor()
  self.cursor.execute ("""CREATE TABLE IF NOT EXISTS campos(NOMBRE TEXT NOT NULL, APELLIDO TEXT NOT NULL, LOCALIDAD TEXT NOT NULL)""" )
  self.con.commit()

 # Evento del boton Guardar
 def btn_Guardar_clicked(self):

  self.con = sqlite3.connect("/home/diego123/Escritorio/pyqt4/prueba.bd")
  self.cursor = self.con.cursor()

  # Datos
  self.nombre = str(self.lineEdit.text())
  self.apellido = str(self.lineEdit_2.text())
  self.localidad = str(self.lineEdit_3.text())
  self.datos = (self.nombre, self.apellido, self.localidad)

  # Inserta los datos en la tabla campos
  self.cursor.execute("INSERT INTO campos (nombre, apellido, localidad) VALUES (?,?,?)", self.datos)
  self.con.commit()

  # Quedan los campos vacios al guardar cliente
  self.lineEdit.setText("")
  self.lineEdit_2.setText("")
  self.lineEdit_3.setText("")

  self.con.commit()
  self.con.close()

 # Evento del boton Caragar
 def btn_Cargar_clicked(self):

  self.con = sqlite3.connect("/home/diego123/Escritorio/pyqt4/prueba.bd")
  self.cursor = self.con.cursor()

  # Se cargan los datos indicados de la tabla
  self.cursor.execute("SELECT NOMBRE, APELLIDO, LOCALIDAD FROM campos")

  # Al presionar el boton lo primero es borrar todos los datos
  self.lista.clear()

  # Se agregan los elementos al QListWidget
  for i in self.cursor:
   self.nombre = str(i[0])
   self.apellido = str(i[1])
   self.localidad = str(i[2])

   self.lista.addItem(self.nombre + " - " + self.apellido + " - " + self.localidad)

  self.con.commit()
  self.con.close()


app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()