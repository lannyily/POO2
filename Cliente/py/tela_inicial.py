# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_inicial.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tela_inicial(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1213, 815)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 200, 731, 561))
        self.label.setStyleSheet("border: 1px solid black;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../imagens/foto3.png"))
        self.label.setObjectName("label")
        self.pushButton_casa_pol = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_casa_pol.setGeometry(QtCore.QRect(450, 650, 16, 16))
        self.pushButton_casa_pol.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_casa_pol.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 255, 0);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}")
        self.pushButton_casa_pol.setText("")
        self.pushButton_casa_pol.setObjectName("pushButton_casa_pol")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 580, 51, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../imagens/foto4.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_rosario = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rosario.setGeometry(QtCore.QRect(350, 660, 16, 16))
        self.pushButton_rosario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_rosario.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 255, 0);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}")
        self.pushButton_rosario.setText("")
        self.pushButton_rosario.setObjectName("pushButton_rosario")
        self.pushButton_matriz = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_matriz.setGeometry(QtCore.QRect(400, 420, 16, 16))
        self.pushButton_matriz.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_matriz.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 255, 0);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}")
        self.pushButton_matriz.setText("")
        self.pushButton_matriz.setObjectName("pushButton_matriz")
        self.pushButton_museu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_museu.setGeometry(QtCore.QRect(360, 390, 16, 16))
        self.pushButton_museu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_museu.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 0, 255);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}")
        self.pushButton_museu.setText("")
        self.pushButton_museu.setObjectName("pushButton_museu")
        self.pushButton_12janelas = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12janelas.setGeometry(QtCore.QRect(340, 470, 16, 16))
        self.pushButton_12janelas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12janelas.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 0, 255);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}")
        self.pushButton_12janelas.setText("")
        self.pushButton_12janelas.setObjectName("pushButton_12janelas")
        self.pushButton_casa_canela = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_casa_canela.setGeometry(QtCore.QRect(500, 550, 16, 16))
        self.pushButton_casa_canela.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_casa_canela.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 0, 255);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}")
        self.pushButton_casa_canela.setText("")
        self.pushButton_casa_canela.setObjectName("pushButton_casa_canela")
        self.pushButton_major = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_major.setGeometry(QtCore.QRect(280, 490, 16, 16))
        self.pushButton_major.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_major.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 0, 255);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}")
        self.pushButton_major.setText("")
        self.pushButton_major.setObjectName("pushButton_major")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 480, 61, 71))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../imagens/foto5.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 590, 81, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../imagens/foto6.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 350, 71, 71))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../imagens/foto7.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 320, 61, 71))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../imagens/foto8.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 400, 61, 71))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../imagens/foto9.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(250, 420, 61, 71))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../imagens/foto10.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 1141, 171))
        self.widget.setStyleSheet("background-color: rgb(255, 222, 124);")
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(580, 50, 152, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_restaurante = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_restaurante.setFont(font)
        self.pushButton_restaurante.setStyleSheet("QPushButton {\n"
"           \n"
"    background-color: rgb(111, 125, 255);\n"
"           border: none;\n"
"           color: white;\n"
"           padding: 10px 20px;\n"
"           text-align: center;\n"
"           text-decoration: none;\n"
"           display: inline-block;\n"
"           font-size: 16px;\n"
"           margin: 4px 2px;\n"
"           cursor: pointer;\n"
"           border-radius: 8px;\n"
"        }\n"
"        QPushButton:hover {\n"
"           background-color: rgb(85, 170, 255); \n"
"        }")
        self.pushButton_restaurante.setObjectName("pushButton_restaurante")
        self.verticalLayout_2.addWidget(self.pushButton_restaurante)
        self.pushButton_hotel = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_hotel.setStyleSheet("QPushButton {\n"
"           \n"
"    background-color: rgb(111, 125, 255);\n"
"           border: none;\n"
"           color: white;\n"
"           padding: 10px 20px;\n"
"           text-align: center;\n"
"           text-decoration: none;\n"
"           display: inline-block;\n"
"           font-size: 16px;\n"
"           margin: 4px 2px;\n"
"           cursor: pointer;\n"
"           border-radius: 8px;\n"
"        }\n"
"        QPushButton:hover {\n"
"           background-color: rgb(85, 170, 255); \n"
"        }")
        self.pushButton_hotel.setObjectName("pushButton_hotel")
        self.verticalLayout_2.addWidget(self.pushButton_hotel)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 321, 161))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../imagens/logo.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.pushButton_sair = QtWidgets.QPushButton(self.widget)
        self.pushButton_sair.setGeometry(QtCore.QRect(1000, 120, 121, 41))
        self.pushButton_sair.setStyleSheet("QPushButton {\n"
"           \n"
"    background-color: rgb(111, 125, 255);\n"
"           border: none;\n"
"           color: white;\n"
"           padding: 10px 20px;\n"
"           text-align: center;\n"
"           text-decoration: none;\n"
"           display: inline-block;\n"
"           font-size: 16px;\n"
"           margin: 4px 2px;\n"
"           cursor: pointer;\n"
"           border-radius: 8px;\n"
"        }\n"
"        QPushButton:hover {\n"
"           background-color: rgb(85, 170, 255); \n"
"        }")
        self.pushButton_sair.setObjectName("pushButton_sair")
        self.perfilButton = QtWidgets.QPushButton(self.widget)
        self.perfilButton.setGeometry(QtCore.QRect(1020, 30, 81, 81))
        self.perfilButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.perfilButton.setStyleSheet("QPushButton {\n"
"    font-size: 30px;\n"
"    border-radius: 40px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton[objectName=\"perfilButton\"] {\n"
"    qproperty-toolTip: \"Perfil\";\n"
"}\n"
"\n"
"QToolTip {\n"
"    font-family: \'SansSerif\';\n"
"    font-size: 10pt;\n"
"}\n"
"")
        self.perfilButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/perfil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.perfilButton.setIcon(icon)
        self.perfilButton.setIconSize(QtCore.QSize(80, 80))
        self.perfilButton.setObjectName("perfilButton")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(770, 200, 391, 561))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 389, 559))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(0, -70, 371, 251))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("../imagens/excursao1.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.pushButton_fe = QtWidgets.QPushButton(self.frame)
        self.pushButton_fe.setGeometry(QtCore.QRect(-10, 140, 391, 41))
        self.pushButton_fe.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_fe.setStyleSheet("\n"
"QPushButton {\n"
"           \n"
"    background-color: rgb(111, 125, 255);\n"
"           border: none;\n"
"           color: white;\n"
"           text-align: center;\n"
"           text-decoration: none;\n"
"           display: inline-block;\n"
"           font-size: 16px;\n"
"           margin: 4px 2px;\n"
"           cursor: pointer;\n"
"           border-radius: 8px;\n"
"            font-weight: bold;\n"
"        }\n"
"        QPushButton:hover {\n"
"           background-color: rgb(85, 170, 255); \n"
"        }\n"
"   ")
        self.pushButton_fe.setCheckable(False)
        self.pushButton_fe.setObjectName("pushButton_fe")
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(0, -20, 371, 221))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("../imagens/excursao2.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.pushButton_cult = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_cult.setGeometry(QtCore.QRect(-20, 140, 401, 41))
        self.pushButton_cult.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_cult.setStyleSheet("\n"
"QPushButton {\n"
"           \n"
"    background-color: rgb(111, 125, 255);\n"
"           border: none;\n"
"           color: white;\n"
"           text-align: center;\n"
"           text-decoration: none;\n"
"           display: inline-block;\n"
"           font-size: 15px;\n"
"           margin: 4px 2px;\n"
"           cursor: pointer;\n"
"           border-radius: 8px;\n"
" font-weight: bold;\n"
"        }\n"
"        QPushButton:hover {\n"
"           background-color: rgb(85, 170, 255); \n"
"        }\n"
"   ")
        self.pushButton_cult.setObjectName("pushButton_cult")
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(0, -50, 371, 231))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("../imagens/excursao3.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.pushButton_his = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_his.setGeometry(QtCore.QRect(-10, 140, 391, 41))
        self.pushButton_his.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_his.setStyleSheet("\n"
"QPushButton {\n"
"           \n"
"    background-color: rgb(111, 125, 255);\n"
"           border: none;\n"
"           color: white;\n"
"           text-align: center;\n"
"           text-decoration: none;\n"
"           display: inline-block;\n"
"           font-size: 15px;\n"
"           margin: 4px 2px;\n"
"           cursor: pointer;\n"
"           border-radius: 8px;\n"
" font-weight: bold;\n"
"        }\n"
"        QPushButton:hover {\n"
"           background-color: rgb(85, 170, 255); \n"
"        }\n"
"   ")
        self.pushButton_his.setObjectName("pushButton_his")
        self.verticalLayout.addWidget(self.frame_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 200, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(92, 160, 212);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1213, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.label_9.setPixmap(QtGui.QPixmap("Cliente/imagens/logo.png"))
        self.label.setPixmap(QtGui.QPixmap("Cliente/imagens/foto3.png"))
        self.label_2.setPixmap(QtGui.QPixmap("Cliente/imagens/foto4.png"))
        self.label_3.setPixmap(QtGui.QPixmap("Cliente/imagens/foto5.png"))
        self.label_4.setPixmap(QtGui.QPixmap("Cliente/imagens/foto6.png"))
        self.label_5.setPixmap(QtGui.QPixmap("Cliente/imagens/foto7.png"))
        self.label_6.setPixmap(QtGui.QPixmap("Cliente/imagens/foto8.png"))
        self.label_7.setPixmap(QtGui.QPixmap("Cliente/imagens/foto9.png"))
        self.label_8.setPixmap(QtGui.QPixmap("Cliente/imagens/foto10.png"))
        self.label_11.setPixmap(QtGui.QPixmap("Cliente/imagens/excursao1.png"))
        self.label_12.setPixmap(QtGui.QPixmap("Cliente/imagens/excursao2.png"))
        self.label_13.setPixmap(QtGui.QPixmap("Cliente/imagens/excursao3.png"))
        self.perfilButton.setIcon(QtGui.QIcon("Cliente/imagens/perfil.png"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_restaurante.setText(_translate("MainWindow", "Restaurantes "))
        self.pushButton_hotel.setText(_translate("MainWindow", "Hotéis "))
        self.pushButton_sair.setText(_translate("MainWindow", "SAIR"))
        self.pushButton_fe.setText(_translate("MainWindow", "Caminho Espiritual: A Capital da Fé"))
        self.pushButton_cult.setText(_translate("MainWindow", "Herança e Identidade: Riquezas e Tradições"))
        self.pushButton_his.setText(_translate("MainWindow", "Raízes Históricas: Uma Jornada pelo Passado"))
        self.label_10.setText(_translate("MainWindow", " Pontos Históricos "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_tela_inicial()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
