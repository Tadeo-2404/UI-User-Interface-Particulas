# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(497, 456)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionPuntos_Cercanos = QAction(MainWindow)
        self.actionPuntos_Cercanos.setObjectName(u"actionPuntos_Cercanos")
        self.actionAlgoritmos = QAction(MainWindow)
        self.actionAlgoritmos.setObjectName(u"actionAlgoritmos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.particular_container = QGroupBox(self.tab)
        self.particular_container.setObjectName(u"particular_container")
        self.particular_container.setStyleSheet(u"background-color: rgb(187, 199, 195);\n"
"padding: 3px;")
        self.gridLayout = QGridLayout(self.particular_container)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_origenX = QLabel(self.particular_container)
        self.label_origenX.setObjectName(u"label_origenX")
        self.label_origenX.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_origenX, 1, 0, 1, 1)

        self.label_origenY = QLabel(self.particular_container)
        self.label_origenY.setObjectName(u"label_origenY")
        self.label_origenY.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_origenY, 2, 0, 1, 1)

        self.label_red = QLabel(self.particular_container)
        self.label_red.setObjectName(u"label_red")
        self.label_red.setStyleSheet(u"text-transform: uppercase;\n"
"")

        self.gridLayout.addWidget(self.label_red, 6, 0, 1, 1)

        self.label_id = QLabel(self.particular_container)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_id, 0, 0, 1, 1)

        self.input_destinoY = QSpinBox(self.particular_container)
        self.input_destinoY.setObjectName(u"input_destinoY")
        self.input_destinoY.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_destinoY.setMaximum(500)

        self.gridLayout.addWidget(self.input_destinoY, 4, 1, 1, 1)

        self.input_origenY = QSpinBox(self.particular_container)
        self.input_origenY.setObjectName(u"input_origenY")
        self.input_origenY.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_origenY.setMaximum(500)

        self.gridLayout.addWidget(self.input_origenY, 2, 1, 1, 1)

        self.label_destinoX = QLabel(self.particular_container)
        self.label_destinoX.setObjectName(u"label_destinoX")
        self.label_destinoX.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_destinoX, 3, 0, 1, 1)

        self.input_blue = QSpinBox(self.particular_container)
        self.input_blue.setObjectName(u"input_blue")
        self.input_blue.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_blue.setMaximum(255)

        self.gridLayout.addWidget(self.input_blue, 8, 1, 1, 1)

        self.agregarFinal_btn = QPushButton(self.particular_container)
        self.agregarFinal_btn.setObjectName(u"agregarFinal_btn")
        self.agregarFinal_btn.setStyleSheet(u"border: none;\n"
"outline: none;\n"
"text-transform: uppercase;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(226, 0, 0);\n"
"\n"
"")

        self.gridLayout.addWidget(self.agregarFinal_btn, 10, 0, 1, 2)

        self.label_green = QLabel(self.particular_container)
        self.label_green.setObjectName(u"label_green")
        self.label_green.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_green, 7, 0, 1, 1)

        self.input_velocidad = QSpinBox(self.particular_container)
        self.input_velocidad.setObjectName(u"input_velocidad")
        self.input_velocidad.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")

        self.gridLayout.addWidget(self.input_velocidad, 5, 1, 1, 1)

        self.input_green = QSpinBox(self.particular_container)
        self.input_green.setObjectName(u"input_green")
        self.input_green.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_green.setMaximum(255)

        self.gridLayout.addWidget(self.input_green, 7, 1, 1, 1)

        self.agregarInicio_btn = QPushButton(self.particular_container)
        self.agregarInicio_btn.setObjectName(u"agregarInicio_btn")
        self.agregarInicio_btn.setStyleSheet(u"border: none;\n"
"outline: none;\n"
"text-transform: uppercase;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(226, 0, 0);\n"
"\n"
"")

        self.gridLayout.addWidget(self.agregarInicio_btn, 9, 0, 1, 2)

        self.label_destinoY = QLabel(self.particular_container)
        self.label_destinoY.setObjectName(u"label_destinoY")
        self.label_destinoY.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_destinoY, 4, 0, 1, 1)

        self.input_id = QSpinBox(self.particular_container)
        self.input_id.setObjectName(u"input_id")
        self.input_id.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_id.setMaximum(500)

        self.gridLayout.addWidget(self.input_id, 0, 1, 1, 1)

        self.input_origenX = QSpinBox(self.particular_container)
        self.input_origenX.setObjectName(u"input_origenX")
        self.input_origenX.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_origenX.setMaximum(500)

        self.gridLayout.addWidget(self.input_origenX, 1, 1, 1, 1)

        self.input_red = QSpinBox(self.particular_container)
        self.input_red.setObjectName(u"input_red")
        self.input_red.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_red.setMaximum(255)

        self.gridLayout.addWidget(self.input_red, 6, 1, 1, 1)

        self.label_velocidad = QLabel(self.particular_container)
        self.label_velocidad.setObjectName(u"label_velocidad")
        self.label_velocidad.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_velocidad, 5, 0, 1, 1)

        self.input_destinoX = QSpinBox(self.particular_container)
        self.input_destinoX.setObjectName(u"input_destinoX")
        self.input_destinoX.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_destinoX.setMaximum(500)

        self.gridLayout.addWidget(self.input_destinoX, 3, 1, 1, 1)

        self.label_blue = QLabel(self.particular_container)
        self.label_blue.setObjectName(u"label_blue")
        self.label_blue.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_blue, 8, 0, 1, 1)

        self.mostrarTodo_btn = QPushButton(self.particular_container)
        self.mostrarTodo_btn.setObjectName(u"mostrarTodo_btn")
        self.mostrarTodo_btn.setStyleSheet(u"border: none;\n"
"outline: none;\n"
"text-transform: uppercase;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(226, 0, 0);\n"
"\n"
"")

        self.gridLayout.addWidget(self.mostrarTodo_btn, 11, 0, 1, 2)


        self.gridLayout_3.addWidget(self.particular_container, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(167, 16777215))
        self.plainTextEdit.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_3.addWidget(self.plainTextEdit, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.input_buscar = QLineEdit(self.tab_2)
        self.input_buscar.setObjectName(u"input_buscar")
        self.input_buscar.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.input_buscar, 1, 0, 1, 1)

        self.btn_buscar = QPushButton(self.tab_2)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.btn_buscar.setStyleSheet(u"border: none;\n"
"outline: none;\n"
"text-transform: uppercase;\n"
"padding: 2px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(226, 0, 0);\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.btn_buscar, 1, 1, 1, 1)

        self.btn_mostrar = QPushButton(self.tab_2)
        self.btn_mostrar.setObjectName(u"btn_mostrar")
        self.btn_mostrar.setStyleSheet(u"border: none;\n"
"outline: none;\n"
"text-transform: uppercase;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(226, 0, 0);\n"
"padding: 2px;\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.btn_mostrar, 1, 2, 1, 1)

        self.table = QTableWidget(self.tab_2)
        self.table.setObjectName(u"table")
        self.table.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.table, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.btn_dibujar = QPushButton(self.tab_3)
        self.btn_dibujar.setObjectName(u"btn_dibujar")
        self.btn_dibujar.setStyleSheet(u"border: none;\n"
"outline: none;\n"
"text-transform: uppercase;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(226, 0, 0);\n"
"padding: 2px;\n"
"\n"
"")

        self.gridLayout_5.addWidget(self.btn_dibujar, 1, 0, 1, 1)

        self.btn_limpiar = QPushButton(self.tab_3)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setStyleSheet(u"border: none;\n"
"outline: none;\n"
"text-transform: uppercase;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(226, 0, 0);\n"
"padding: 2px;\n"
"\n"
"")

        self.gridLayout_5.addWidget(self.btn_limpiar, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_6 = QGridLayout(self.tab_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.btnSort_velocidad = QPushButton(self.tab_4)
        self.btnSort_velocidad.setObjectName(u"btnSort_velocidad")
        self.btnSort_velocidad.setStyleSheet(u"border: none;\n"
"outline: none;\n"
"text-transform: uppercase;\n"
"padding: 2px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(226, 0, 0);\n"
"\n"
"")

        self.gridLayout_6.addWidget(self.btnSort_velocidad, 1, 2, 1, 1)

        self.btnSort_distancia = QPushButton(self.tab_4)
        self.btnSort_distancia.setObjectName(u"btnSort_distancia")
        self.btnSort_distancia.setStyleSheet(u"border: none;\n"
"outline: none;\n"
"text-transform: uppercase;\n"
"padding: 2px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(226, 0, 0);\n"
"\n"
"")

        self.gridLayout_6.addWidget(self.btnSort_distancia, 1, 1, 1, 1)

        self.btnSort_id = QPushButton(self.tab_4)
        self.btnSort_id.setObjectName(u"btnSort_id")
        self.btnSort_id.setStyleSheet(u"border: none;\n"
"outline: none;\n"
"text-transform: uppercase;\n"
"padding: 2px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(226, 0, 0);\n"
"\n"
"")

        self.gridLayout_6.addWidget(self.btnSort_id, 1, 0, 1, 1)

        self.plainTextEditSort = QPlainTextEdit(self.tab_4)
        self.plainTextEditSort.setObjectName(u"plainTextEditSort")
        self.plainTextEditSort.setStyleSheet(u"width: 100%;")

        self.gridLayout_6.addWidget(self.plainTextEditSort, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 497, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuVer = QMenu(self.menubar)
        self.menuVer.setObjectName(u"menuVer")
        self.menuAlgoritmos = QMenu(self.menubar)
        self.menuAlgoritmos.setObjectName(u"menuAlgoritmos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())
        self.menubar.addAction(self.menuAlgoritmos.menuAction())
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuVer.addAction(self.actionPuntos_Cercanos)
        self.menuAlgoritmos.addAction(self.actionAlgoritmos)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionPuntos_Cercanos.setText(QCoreApplication.translate("MainWindow", u"Puntos ", None))
        self.actionAlgoritmos.setText(QCoreApplication.translate("MainWindow", u"Puntos Cercanos", None))
        self.particular_container.setTitle(QCoreApplication.translate("MainWindow", u"UI-Particulas", None))
        self.label_origenX.setText(QCoreApplication.translate("MainWindow", u"Origen X", None))
        self.label_origenY.setText(QCoreApplication.translate("MainWindow", u"Origen Y", None))
        self.label_red.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_destinoX.setText(QCoreApplication.translate("MainWindow", u"Destino X", None))
        self.agregarFinal_btn.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.label_green.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.agregarInicio_btn.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.label_destinoY.setText(QCoreApplication.translate("MainWindow", u"Destino Y", None))
        self.label_velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_blue.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.mostrarTodo_btn.setText(QCoreApplication.translate("MainWindow", u"Mostrar todo", None))
        self.plainTextEdit.setPlainText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.input_buscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introduce el ID a buscar", None))
        self.btn_buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btn_mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btn_dibujar.setText(QCoreApplication.translate("MainWindow", u"DIBUJAR", None))
        self.btn_limpiar.setText(QCoreApplication.translate("MainWindow", u"LIMPIAR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.btnSort_velocidad.setText(QCoreApplication.translate("MainWindow", u"sort velocidad", None))
        self.btnSort_distancia.setText(QCoreApplication.translate("MainWindow", u"sort distancia", None))
        self.btnSort_id.setText(QCoreApplication.translate("MainWindow", u"sort id", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Ordenar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuVer.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.menuAlgoritmos.setTitle(QCoreApplication.translate("MainWindow", u"Algoritmos", None))
    # retranslateUi

