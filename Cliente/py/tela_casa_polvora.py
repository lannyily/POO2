# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_casa_polvora.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tela_casa_polvora(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1176, 721)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 150, 371, 281))
        self.label.setStyleSheet("border: 1px solid black;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../imagens/foto12.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 440, 371, 231))
        self.label_2.setStyleSheet("border: 1px solid black;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../imagens/foto11.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 0, 1151, 141))
        self.widget.setStyleSheet("background-color: rgb(255, 222, 124);")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(-10, -10, 341, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../imagens/logo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton_perfil = QtWidgets.QPushButton(self.widget)
        self.pushButton_perfil.setGeometry(QtCore.QRect(1040, 20, 81, 81))
        self.pushButton_perfil.setStyleSheet("QPushButton {\n"
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
        self.pushButton_perfil.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/perfil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_perfil.setIcon(icon)
        self.pushButton_perfil.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_perfil.setObjectName("pushButton_perfil")
        self.pushButton_voltar = QtWidgets.QPushButton(self.widget)
        self.pushButton_voltar.setGeometry(QtCore.QRect(880, 70, 139, 41))
        self.pushButton_voltar.setStyleSheet("QPushButton {\n"
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
        self.pushButton_voltar.setObjectName("pushButton_voltar")
        self.pushButton_sair = QtWidgets.QPushButton(self.widget)
        self.pushButton_sair.setGeometry(QtCore.QRect(880, 20, 139, 41))
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(930, 610, 231, 51))
        self.pushButton.setStyleSheet("QPushButton {\n"
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
"           border: 2px solid #335fff;\n"
"        }\n"
"        QPushButton:hover {\n"
"           background-color: rgb(85, 170, 255); \n"
"        }")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 160, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(58, 0, 173);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 220, 741, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 360, 131, 41))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"     /* Cor de fundo vermelha - você pode ajustar conforme necessário */\n"
"    \n"
"    background-color: rgb(3, 3, 3);\n"
"    border: 2px solid #BB0000;  /* Cor da borda */\n"
"    color: #FFFFFF;  /* Cor do texto */\n"
"    padding: 5px 10px;  /* Espaçamento interno */\n"
"    border-radius: 5px;  /* Borda arredondada */\n"
" font-size: 14px;  /* Tamanho da fonte ajustado para 14 pixels */\n"
"    font-weight: bold;  /* Fonte em negrito */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #CC0000;  /* Cor de fundo ao passar o mouse */\n"
"    border: 2px solid #990000;  /* Cor da borda ao passar o mouse */\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagens/youtube.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 360, 151, 41))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: #ffffff;  /* Cor de fundo branca */\n"
"    border: 2px solid #dddddd;  /* Cor da borda */\n"
"    color: #333333;  /* Cor do texto */\n"
"    padding: 10px 15px;  /* Espaçamento interno ajustado para um botão maior */\n"
"    border-radius: 5px;  /* Borda arredondada */\n"
"    font-size: 14px;  /* Tamanho da fonte ajustado para 14 pixels */\n"
"    font-weight: bold;  /* Fonte em negrito */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;  /* Cor de fundo ao passar o mouse */\n"
"    border: 2px solid #cccccc;  /* Cor da borda ao passar o mouse */\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../imagens/maps.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1176, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.label_3.setPixmap(QtGui.QPixmap("Cliente/imagens/logo.png"))
        self.label.setPixmap(QtGui.QPixmap("Cliente/imagens/foto12.jpg"))
        self.label_2.setPixmap(QtGui.QPixmap("Cliente/imagens/foto11.jpg"))
        self.pushButton_perfil.setIcon(QtGui.QIcon("Cliente/imagens/perfil.png"))
        self.pushButton_2.setIcon(QtGui.QIcon("Cliente/imagens/youtube.png"))
        self.pushButton_3.setIcon(QtGui.QIcon("Cliente/imagens/maps.png"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_voltar.setText(_translate("MainWindow", "Voltar"))
        self.pushButton_sair.setText(_translate("MainWindow", "SAIR"))
        self.pushButton.setText(_translate("MainWindow", "Reservar visita"))
        self.label_4.setText(_translate("MainWindow", "Casa da pólvora"))
        self.label_5.setText(_translate("MainWindow", "Conheça o museu mais antigo do Piauí. A Casa da Pólvora é uma construção de uma \n"
"única sala de pedras toscas e rejuntadas com argamassa de barro e representa o grande \n"
"momento militar do Piauí. Construção datada do início do século XIX para abrigar a fábrica \n"
"de pólvora, edificada sobre um único lajedo, às margens do riacho Pouca Vergonha é o \n"
"marco da emancipação do Piauí, durante as lutas pela independência.\n"
""))
        self.pushButton_2.setText(_translate("MainWindow", "Vídeo "))
        self.pushButton_3.setText(_translate("MainWindow", "Localização"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_tela_casa_polvora()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
