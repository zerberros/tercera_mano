#!/usr/bin/python

#pyside-uic -o tercera_manoUI.py ./gui/tercera-manoUI.ui
###############################################################################
# Copyleft (c) 2013 Jairo Estefanía. Some rights reserved.                    #
# This program or module is free software: you can redistribute it and/or     #
# modify it under the terms of the GNU General Public Licence as published    #
# by the Free Software Foundation, either version 2 of the Licence, or        #
# version 3 of the Licence, or (at your option) any later version. It is      #
# provided for educational purposes and is distributed in the hope that       #
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied       #
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See        #
# the GNU General Public Licence for more details.                            #
###############################################################################

#codigo para transformar el archivo de Qt-designer a un script python:
#pyside-uic -o tercera_manoUI.py ./gui/tercera-manoUI.ui

#importar las bibliotecas necesarias:
import sys
import platform  # Test
import PySide  # Test
#import sympy  # Test
from PySide import QtCore, QtGui
from PySide.QtGui import QApplication, QMainWindow, QTextEdit, QPushButton,  QMessageBox #test
from tercera_manoUI import Ui_MainWindow
from sympy import integrate, erf, exp, sin, sqrt, log, oo, pi, sinh, symbols
from sympy import *

__version__ = '0.0.2'


class ControlMainWindow(QtGui.QMainWindow):
	''' Do not have any help for now '''

	def sumaserie(self, x, y):
		return (x + y)

	def sumaparalelo(self, x, y):
		return ((x * y) / (x + y))

	def asociacion_de_impedancias(self):
		a = complex(self.ui.lineEdit.text())
		b = complex(self.ui.lineEdit_2.text())
		self.ui.label_3.setText("Valor Serie: " + str(self.sumaserie(a, b)))
		self.ui.label_4.setText("Valor Paralelo: " + str(self.sumaparalelo(a, b)))

	def estrella_triangulo(self):
		z1 = complex(self.ui.lE_dt_1.text())
		z2 = complex(self.ui.lE_dt_2.text())
		z3 = complex(self.ui.lE_dt_3.text())
		if self.ui.cB_dt.currentText() == 'Estrella -> Triángulo':

			Z1 = (z2 + z3 + (z2 * z3) / z1)
			Z2 = (z1 + z3 + (z1 * z3) / z2)
			Z3 = (z1 + z2 + (z1 * z2) / z3)
		elif self.ui.cB_dt.currentText() == 'Triángulo -> Estrella':

			Z1 = (z2 * z3) / (z1 + z2 + z3)
			Z2 = (z1 * z3) / (z1 + z2 + z3)
			Z3 = (z1 * z2) / (z1 + z2 + z3)
		self.ui.lb_dt_1.setText(str(Z1))
		self.ui.lb_dt_2.setText(str(Z2))
		self.ui.lb_dt_3.setText(str(Z3))



	def integrar(self):

		f = self.ui.lineEdit_int_funcion.text()

		f_var = [Symbol(self.ui.lineEdit_int_var_1.text())\
		, Symbol(self.ui.lineEdit_int_var_2.text())\
		, Symbol(self.ui.lineEdit_int_var_3.text())]

		f_min = [(self.ui.lineEdit_int_min_1.text()), (self.ui.lineEdit_int_min_2.text()),(self.ui.lineEdit_int_min_3.text())]

		f_max = [(self.ui.lineEdit_int_max_1.text()),(self.ui.lineEdit_int_max_2.text()),(self.ui.lineEdit_int_max_3.text())]

		for i in range(0, int(self.ui.spinBox_int.text())):
			if self.ui.radioButton_int_def.isChecked() == True:
				f = integrate(f,(f_var[i],f_min[i],f_max[i]))
				self.ui.label_int_solucion.setText(str(f))
				print (f)

			else:
				f = integrate(f,f_var[i])
				self.ui.label_int_solucion.setText(str(f))
				print (f)

	def derivar(self):
		f=self.ui.lineEdit_int_funcion.text()
		f_var=[Symbol(self.ui.lineEdit_int_var_1.text()), Symbol(self.ui.lineEdit_int_var_2.text()), Symbol(self.ui.lineEdit_int_var_3.text())]
		for i in range(0,int(self.ui.spinBox_int.text())):
			f=diff(f,f_var[i])
			self.ui.label_int_solucion.setText(str(f))

	def test_spin(self):
		# Esto es para desactibar las entradas de texto de los limites
		# y variables de integracion que no se vayan a usar, porque se quiera hacer una integral simple, por ejemplo.
		if int(self.ui.spinBox_int.text()) == 1:
			self.ui.label_int_text_2.setEnabled(False)
			self.ui.label_int_min_2.setEnabled(False)
			self.ui.label_int_max_2.setEnabled(False)
			self.ui.lineEdit_int_var_2.setEnabled(False)
			self.ui.lineEdit_int_min_2.setEnabled(False)
			self.ui.lineEdit_int_max_2.setEnabled(False)
			self.ui.label_int_text_3.setEnabled(False)
			self.ui.label_int_min_3.setEnabled(False)
			self.ui.label_int_max_3.setEnabled(False)
			self.ui.lineEdit_int_var_3.setEnabled(False)
			self.ui.lineEdit_int_min_3.setEnabled(False)
			self.ui.lineEdit_int_max_3.setEnabled(False)
		elif int(self.ui.spinBox_int.text()) == 2:
			self.ui.label_int_text_2.setEnabled(True)
			self.ui.label_int_min_2.setEnabled(True)
			self.ui.label_int_max_2.setEnabled(True)
			self.ui.lineEdit_int_var_2.setEnabled(True)
			self.ui.lineEdit_int_min_2.setEnabled(True)
			self.ui.lineEdit_int_max_2.setEnabled(True)
			self.ui.label_int_text_3.setEnabled(False)
			self.ui.label_int_min_3.setEnabled(False)
			self.ui.label_int_max_3.setEnabled(False)
			self.ui.lineEdit_int_var_3.setEnabled(False)
			self.ui.lineEdit_int_min_3.setEnabled(False)
			self.ui.lineEdit_int_max_3.setEnabled(False)
		elif int(self.ui.spinBox_int.text()) == 3:
			self.ui.label_int_text_2.setEnabled(True)
			self.ui.label_int_min_2.setEnabled(True)
			self.ui.label_int_max_2.setEnabled(True)
			self.ui.lineEdit_int_var_2.setEnabled(True)
			self.ui.lineEdit_int_min_2.setEnabled(True)
			self.ui.lineEdit_int_max_2.setEnabled(True)
			self.ui.label_int_text_3.setEnabled(True)
			self.ui.label_int_min_3.setEnabled(True)
			self.ui.label_int_max_3.setEnabled(True)
			self.ui.lineEdit_int_var_3.setEnabled(True)
			self.ui.lineEdit_int_min_3.setEnabled(True)
			self.ui.lineEdit_int_max_3.setEnabled(True)

	def about(self):
		'''Popup a box with about message.'''

		QMessageBox.about(self, "tercera-mano",
				"""<b>Tercera-mano</b> v %s
				<p>Copyleft - 2013 Jairo Estefania.
				<p>Some rights reserved in accordance with
				GPL v2 or later - NO WARRANTIES!
				<p>Enjoy   ;)
				<p>Python %s - sympy version %s -  PySide version %s - Qt version %s on %s """ % (__version__,
				platform.python_version(), sympy.__version__, PySide.__version__,  PySide.QtCore.__version__,
				platform.system()))

	def __init__(self, parent=None):
		super(ControlMainWindow, self).__init__(parent)
		# Esto es siempre lo mismo

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# conexiones entre los eventos de la GUI y las funciones
		QtCore.QObject.connect(self.ui.pushButton_calculo_impedancias, QtCore.SIGNAL("clicked()"), self.asociacion_de_impedancias)
		QtCore.QObject.connect(self.ui.pushButton_integra, QtCore.SIGNAL("clicked()"), self.integrar)
		QtCore.QObject.connect(self.ui.pushButton_deriva, QtCore.SIGNAL("clicked()"), self.derivar)
		QtCore.QObject.connect(self.ui.pB_dt_cal, QtCore.SIGNAL("clicked()"), self.estrella_triangulo)
		QtCore.QObject.connect(self.ui.actionAbout,QtCore.SIGNAL("triggered()"), self.about)
		QtCore.QObject.connect(self.ui.spinBox_int, QtCore.SIGNAL("valueChanged(int)"), self.test_spin)



if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	mySW = ControlMainWindow()
	mySW.show()
	sys.exit(app.exec_())
