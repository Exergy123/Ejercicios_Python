__author__ = 'Daniel'

#!/usr/bin/python
# -*- coding: utf-8 -*-

# www.pythondiario.com
# Combinar 2 ComboBox

import sys
from PyQt4 import QtCore, QtGui, uic

# Cargar nuestro archivo .ui
form_class = uic.loadUiType("combobox.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
 def __init__(self, parent=None):
  QtGui.QMainWindow.__init__(self, parent)
  self.setupUi(self)
  #Rellana los datos por primera ves del comboBox_2
  self.llenar_comboBox2()
  #Señal para cambiar, segun la selecccion, el comboBox_2
  QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL("currentIndexChanged(QString)"), self.llenar_comboBox2)
  self.btn_Ver.clicked.connect(self.btn_Ver_clicked)



 # Evento del boton Ver
 def btn_Ver_clicked(self):

  x = self.comboBox_2.currentText()
  self.Resultado.setText(x)

 # Llena el comboBox_2
 def llenar_comboBox2(self):

  python = ["Diego", "Martin", "Lorena"]
  java = ["Sergio", "Maria", "Miguel"]

  self.comboBox_2.clear()
  if self.comboBox.currentText() == "Python":
   self.comboBox_2.addItems(python)
  elif self.comboBox.currentText() == "Java":
   self.comboBox_2.addItems(java)

if __name__ == "__main__":
 app = QtGui.QApplication(sys.argv)
 MyWindow = MyWindowClass(None)
 MyWindow.show()
 app.exec_()