# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'App.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(565, 347)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.RbtnAnio = QRadioButton(self.centralwidget)
        self.RbtnAnio.setObjectName(u"RbtnAnio")
        self.RbtnAnio.setGeometry(QRect(50, 20, 82, 17))
        self.RbtnAutor = QRadioButton(self.centralwidget)
        self.RbtnAutor.setObjectName(u"RbtnAutor")
        self.RbtnAutor.setGeometry(QRect(210, 20, 82, 17))
        self.RbtnDOI = QRadioButton(self.centralwidget)
        self.RbtnDOI.setObjectName(u"RbtnDOI")
        self.RbtnDOI.setGeometry(QRect(420, 20, 82, 17))
        self.txtTexto = QLineEdit(self.centralwidget)
        self.txtTexto.setObjectName(u"txtTexto")
        self.txtTexto.setGeometry(QRect(30, 40, 391, 20))
        self.btnBuscar = QPushButton(self.centralwidget)
        self.btnBuscar.setObjectName(u"btnBuscar")
        self.btnBuscar.setGeometry(QRect(440, 40, 75, 23))
        self.BtnLimpiar = QPushButton(self.centralwidget)
        self.BtnLimpiar.setObjectName(u"BtnLimpiar")
        self.BtnLimpiar.setGeometry(QRect(440, 70, 75, 23))
        self.ListResultados = QListWidget(self.centralwidget)
        self.ListResultados.setObjectName(u"ListResultados")
        self.ListResultados.setGeometry(QRect(300, 110, 256, 192))
        self.lbAutor = QLabel(self.centralwidget)
        self.lbAutor.setObjectName(u"lbAutor")
        self.lbAutor.setGeometry(QRect(10, 110, 47, 13))
        self.lbUri = QLabel(self.centralwidget)
        self.lbUri.setObjectName(u"lbUri")
        self.lbUri.setGeometry(QRect(10, 140, 47, 13))
        self.lbFecha = QLabel(self.centralwidget)
        self.lbFecha.setObjectName(u"lbFecha")
        self.lbFecha.setGeometry(QRect(10, 170, 47, 13))
        self.txtAutor = QLabel(self.centralwidget)
        self.txtAutor.setObjectName(u"txtAutor")
        self.txtAutor.setGeometry(QRect(70, 110, 191, 16))
        self.lbNombre = QLabel(self.centralwidget)
        self.lbNombre.setObjectName(u"lbNombre")
        self.lbNombre.setGeometry(QRect(10, 270, 47, 13))
        self.lbLenguaje = QLabel(self.centralwidget)
        self.lbLenguaje.setObjectName(u"lbLenguaje")
        self.lbLenguaje.setGeometry(QRect(10, 200, 47, 13))
        self.lbVolumen = QLabel(self.centralwidget)
        self.lbVolumen.setObjectName(u"lbVolumen")
        self.lbVolumen.setGeometry(QRect(10, 230, 47, 13))
        self.txtUri = QLabel(self.centralwidget)
        self.txtUri.setObjectName(u"txtUri")
        self.txtUri.setGeometry(QRect(70, 140, 191, 16))
        self.txtFecha = QLabel(self.centralwidget)
        self.txtFecha.setObjectName(u"txtFecha")
        self.txtFecha.setGeometry(QRect(70, 170, 191, 16))
        self.txtLenguaje = QLabel(self.centralwidget)
        self.txtLenguaje.setObjectName(u"txtLenguaje")
        self.txtLenguaje.setGeometry(QRect(70, 200, 191, 16))
        self.txtVolumen = QLabel(self.centralwidget)
        self.txtVolumen.setObjectName(u"txtVolumen")
        self.txtVolumen.setGeometry(QRect(70, 230, 191, 16))
        self.txtNombre = QLabel(self.centralwidget)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(70, 270, 191, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.RbtnAnio.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None))
        self.RbtnAutor.setText(QCoreApplication.translate("MainWindow", u"Autor", None))
        self.RbtnDOI.setText(QCoreApplication.translate("MainWindow", u"DOI", None))
        self.txtTexto.setText("")
        self.btnBuscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.BtnLimpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.lbAutor.setText(QCoreApplication.translate("MainWindow", u"Autor:", None))
        self.lbUri.setText(QCoreApplication.translate("MainWindow", u"Uri:", None))
        self.lbFecha.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.txtAutor.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lbNombre.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.lbLenguaje.setText(QCoreApplication.translate("MainWindow", u"Lenguaje:", None))
        self.lbVolumen.setText(QCoreApplication.translate("MainWindow", u"Volumen:", None))
        self.txtUri.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.txtFecha.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.txtLenguaje.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.txtVolumen.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.txtNombre.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

