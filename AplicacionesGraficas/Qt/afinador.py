__author__ = 'Daniel'

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Afinador de guitarra 1.0
# www.pythondiario.com

import sys
import pygame
import time
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QSound

# Cargar nuestro archivo .ui
form_class = uic.loadUiType("afinador.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btn_MI.clicked.connect(self.btn_MI_clicked)
        self.btn_LA.clicked.connect(self.btn_LA_clicked)
        self.btn_RE.clicked.connect(self.btn_RE_clicked)
        self.btn_SOL.clicked.connect(self.btn_SOL_clicked)
        self.btn_SI.clicked.connect(self.btn_SI_clicked)
        self.btn_mi.clicked.connect(self.btn_mi_clicked)
        self.btn_detener.clicked.connect(self.btn_Detener_clicked)
        pygame.mixer.init()


    def btn_MI_clicked(self):
        pygame.mixer.music.stop()

        pygame.mixer.init()
        pygame.mixer.music.load("/home/diego123/Escritorio/afinador/Tonos/Mi.mp3")
        pygame.mixer.music.play(-1)

    def btn_LA_clicked(self):
        pygame.mixer.music.stop()

        pygame.mixer.init()
        pygame.mixer.music.load("/home/diego123/Escritorio/afinador/Tonos/la.mp3")
        pygame.mixer.music.play(-1)

    def btn_RE_clicked(self):
        pygame.mixer.music.stop()

        pygame.mixer.init()
        pygame.mixer.music.load("/home/diego123/Escritorio/afinador/Tonos/re.mp3")
        pygame.mixer.music.play(-1)

    def btn_SOL_clicked(self):
        pygame.mixer.music.stop()

        pygame.mixer.init()
        pygame.mixer.music.load("/home/diego123/Escritorio/afinador/Tonos/sol.mp3")
        pygame.mixer.music.play(-1)

    def btn_SI_clicked(self):

        pygame.mixer.music.stop()

        pygame.mixer.init()
        pygame.mixer.music.load("/home/diego123/Escritorio/afinador/Tonos/si.mp3")
        pygame.mixer.music.play(-1)

    def btn_mi_clicked(self):

        pygame.mixer.music.stop()


        pygame.mixer.init()
        pygame.mixer.music.load("/home/diego123/Escritorio/afinador/Tonos/mi.mp3")
        pygame.mixer.music.play(-1)



    def btn_Detener_clicked(self):

        pygame.mixer.music.stop()




app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
pygame.init()
MyWindow.show()
app.exec_()